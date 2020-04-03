"""https://wiki.python.org/moin/UdpCommunication"""

import threading
import queue
import logging

import socket
import time


class UDPClient(threading.Thread):
    """UDP Broadcaster"""
    def __init__(self, ip, port,
                 outbound_queue,
                 logger):
        self.ip = ip
        self.port = port
        self.addr = (self.ip, self.port)
        self.outbound_queue = outbound_queue
        self.logger = logger

        self.is_running = True
        super().__init__()

    def run(self):
        self.socket = socket.socket(socket.AF_INET,  # Internet
                                    socket.SOCK_DGRAM)  # UDP

        #print(dir(self.socket))
        #print(self.socket.getsockname())

        while self.is_running:
            if not self.outbound_queue.empty():
                message = self.outbound_queue.get()
                self.logger.info(''.join([
                    f'[{self.addr}]',
                    f'[SEND]: ',
                    f'{message}'
                ]))
                self.socket.sendto(message.encode(), self.addr)


    def stop(self):
        self.is_running = False
        self.socket.close()
        threading.Thread.join(self)


class UDPServer(threading.Thread):
    """UDP Listener"""
    def __init__(self, ip, port,
                 inbound_queue,
                 logger):
        self.ip = ip
        self.port = port
        self.addr = (self.ip, self.port)
        self.inbound_queue = inbound_queue
        self.logger = logger

        self.is_running = True
        super().__init__()

    def run(self):
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_DGRAM)
        self.socket.bind(self.addr)
        
        while self.is_running:
            data, addr = self.socket.recvfrom(1024)
            self.logger.info(''.join([
                    f'[{self.socket.getsockname()}]',
                    f'[{addr}]',
                    f'[RCV]: ',
                    f'{data.decode()}'
                ]))
            self.inbound_queue.put(data.decode())


    def stop(self):
        self.is_running = False
        self.socket.sendto('STOP LISTENING'.encode(), self.addr)
        time.sleep(.1)
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        threading.Thread.join(self)


if __name__ == '__main__':

    ip = "127.0.0.1"
    port = 5005
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    outbound_queue = queue.Queue()
    inbound_queue = queue.Queue()

    broadcaster = UDPClient(ip, port,
                            outbound_queue,
                            logging)
    broadcaster.start()

    
    listener = UDPServer(ip, port,
                         inbound_queue,
                         logging)
    listener.start()


    while True:
        try:
            message = input('UDP Broadcast: ')
            outbound_queue.put(message)
        except KeyboardInterrupt:
            broadcaster.stop()
            listener.stop()
            break
