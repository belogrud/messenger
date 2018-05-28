import socket
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

def main():

    response = Response()
    # print(response.ok)
    print('Server ready.')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 7777))
    s.listen(5)

    try:
        while True:
            client, addr = s.accept()

            response.ok['time'] = str(time.time())
            message_in_json = json.dumps(response.ok)
            message_in_bynary = message_in_json.encode('utf-8')
            client.send(message_in_bynary)

            client.close()
    except KeyboardInterrupt:
        print('Goodbye')
        exit(0)

if __name__ == '__main__':
    main()

