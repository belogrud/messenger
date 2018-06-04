from socket import socket, AF_INET, SOCK_STREAM
import time
import json

#   JIM definitions for a server
class Response:
    def __init__(self):

        # 1xx - information notifications.
        self.basic = {
            'response': '100',
            'time': str(time.time()),
            'alert': 'basic response notification',
        }
        self.urgent = {
            'response': '101',
            'time': str(time.time()),
            'alert': 'urgent response notification',
        }

        # 2xx - finished success notifications.
        self.ok = {
            'response': '200',
            'time': str(time.time()),
            'alert': 'ok',
        }
        self.created = {
            'response': '201',
            'time': str(time.time()),
            'alert': 'created',
        }
        self.accepted = {
            'response': '202',
            'time': str(time.time()),
            'alert': 'accepted',
        }

        # 4xx - errors on client side notifications.
        self.wrong = {
            'response': '400',
            'time': str(time.time()),
            'alert': 'wrong request or json-object',
        }
        self.unauthorized = {
            'response': '401',
            'time': str(time.time()),
            'alert': 'not authorized',
        }
        self.incorrect = {
            'response': '402',
            'time': str(time.time()),
            'alert': 'incorrect login or password',
        }
        self.forbidden = {
            'response': '403',
            'time': str(time.time()),
            'alert': 'user was blocked, access forbidden',
        }
        self.notfound = {
            'response': '404',
            'time': str(time.time()),
            'alert': 'user or chat not found on this server',
        }
        self.conflict = {
            'response': '409',
            'time': str(time.time()),
            'alert': 'conflict was found, user already connected',
        }
        self.gone = {
            'response': '410',
            'time': str(time.time()),
            'alert': 'recipient is present, but not accessible - is in offline state',
        }

        # 5xx - errors on server side notifications.
        self.error = {
            'response': '500',
            'time': str(time.time()),
            'alert': 'error on server side',
        }


if __name__ == '__main__':

    # response = Response()
    # print(response.ok)
    # print('Server ready.')

    server_address = 'localhost'
    server_port = '7777'

    server = socket(AF_INET, SOCK_STREAM)
    server.bind(server_address, server_port)
    server.listen(15)
    server.timeout(0.2)

    clients = []

    while True:
        client, addr = server.accept()

        response = Response()
        response.ok['time'] = str(time.time())
        message_in_json = json.dumps(response.ok)
        message_in_binary = message_in_json.encode('utf-8')

        client.send(message_in_binary)

        client.close()

