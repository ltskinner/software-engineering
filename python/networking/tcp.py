
import threading
import queue
import logging

import socket
import select
import time


class TCPClient(threading.Thread):
    def __init__(self, ip, port,
                 inbound_queue, outbound_queue,
                 logger):
        super().__init__()
        self.ip = ip
        self.port = port
        self.addr = (self.ip, self.port)
        self.inbound_queue = inbound_queue
        self.outbound_queue = outbound_queue

    def run(self):
        self.is_running = True

        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)  # TCP
        self.socket.connect(self.addr)

        self.inputs = [ self.socket ]
        self.outputs = [ self.socket ]

        while self.is_running:
            inbounds, outbounds, _ = select.select(
                self.inputs, self.outputs, [])

            for reader in inbounds:
                if reader is self.socket:
                    data = reader.recv(1024)
                    if data:
                        self.inbound_queue.put(data.decode())

            for writer in outbounds:
                if not self.outbound_queue.empty():
                    message = self.outbound_queue.get()
                    writer.sendall(message.encode())

    def stop(self):
        self.is_running = False
        self.socket.close()
        threading.Thread.join(self)


class TCPServer(threading.Thread):
    def __init__(self, ip, port,
                 inbound_queue, outbound_queue,
                 logger,
                 MAX_CONNECTIONS=1):
        super().__init__()
        self.ip = ip
        self.port = port
        self.addr = (self.ip, self.port)
        self.inbound_queue = inbound_queue
        self.outbound_queue = outbound_queue
        self.MAX_CONNECTIONS = MAX_CONNECTIONS

        self.is_running = True

    def run(self):
        self.is_running = True

        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)  # TCP
        self.socket.setblocking(0)
        self.socket.bind(self.addr)
        self.socket.listen(self.MAX_CONNECTIONS)

        self.inputs = [ self.socket ]
        self.outputs = [ self.socket ]

        while self.is_running:
            inbounds, outbounds, exceptions = select.select(
                self.inputs, self.outputs, self.inputs)
            
            for reader in inbounds:
                if reader._closed:
                    continue
            
                if reader is self.socket:
                    conn, addr = reader.accept()
                    conn.setblocking(0)  # Not hold up the program
                    self.inputs.append(conn)
                else:
                    data = reader.recv(1024)
                    if data:
                        self.inbound_queue.put(data.decode())
                    
                        # Add to outputs for response
                        if reader not in self.outputs:
                            self.outputs.append(reader)
                    else:
                        # Closing
                        self.inputs.remove(reader)
                        if reader in self.outputs:
                            self.outputs.remove(reader)
                        reader.close()
            
            for writer in outbounds:
                if not self.outbound_queue.empty():
                    message = self.outbound_queue.get()
                    writer.sendall(message.encode())
            
            for excepted in exceptions:
                self.inputs.remove(excepted)
                if excepted in self.outputs:
                    self.outputs.remove(excepted)
                    excepted.close()

    def stop(self):
        self.is_running = False
        self.socket.close()
        threading.Thread.join(self)


if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 5005
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    server_inbound_queue = queue.Queue()
    server_outbound_queue = queue.Queue()

    client_inbound_queue = queue.Queue()
    client_outbound_queue = queue.Queue()

    server = TCPServer(ip, port,
                       server_inbound_queue, server_outbound_queue,
                       logging)
    server.start()
    time.sleep(1)

    client = TCPClient(ip, port,
                       client_inbound_queue, client_outbound_queue,
                       logging)
    client.start()

    while True:
        try:
            send_message = input('TCP Message: ')
            client_outbound_queue.put(send_message)
            time.sleep(.5)

            while not server_inbound_queue.empty():
                rcv_message = server_inbound_queue.get()
                logging.info(f'[RCV]: {rcv_message}')
        except KeyboardInterrupt:
            client.stop()
            time.sleep(.5)
            server.stop()
            break
