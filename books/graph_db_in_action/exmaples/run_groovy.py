"""
https://stackoverflow.com/questions/70400302/send-string-gremlin-query-to-amazon-neptune-database-using-tinkerpops-gremlinpy
"""

import argparse
import pprint

from gremlin_python.driver import client
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


from tornado import httpclient

if __name__ == "__main__":

    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('script', type=str, help='The script to run')

    args = parser.parse_args()

    print(args.script)

    with open (args.script,'r') as file:
        query = file.read()
    
    print(query)


    ws_url = 'ws://localhost:8182/gremlin'
    gremlin_client = client.Client(ws_url, "g")

    result = gremlin_client.submit(query)
    future_results = result.all()
    results = future_results.result()


    print('------------------ Results: ------------------')
    pprint.pprint(results)

    gremlin_client.close()
