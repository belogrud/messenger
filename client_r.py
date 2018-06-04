from socket import socket, AF_INET, SOCK_STREAM
import json
import time

#   JIM definitions for a client
class Action:
    def __init__(self):
        self.presence = {
            'action': 'presence',
            'time': str(time.time()),
            'type': 'status',
            'user': {
                'account_name': 'guest',
                'status': 'Yep, I''m here!',
            }
        }
        self.probe = {
            'action': 'probe',
            'time': str(time.time()),
        }
        self.msg = {
            'action': 'msg',
            'time': str(time.time()),
            'from': 'account_name',
            'to': 'account_name',
            'encoding': 'utf-8',
            'message': 'message'
        }
        self.quit = {
            'action': 'quit'
        }
        self.authenticate = {
            'action': 'authenticate',
            'time': str(time.time()),
            'user': {
                'account_name': 'username1',
                'password': 'password1',
            }
        }
        self.join = {
            'action': 'join',
            'time': str(time.time()),
            'room': '#room_name',
        }
        self.leave = {
            'action': 'leave',
            'time': str(time.time()),
            'room': '#room_name'
        }


class TypeOfUsernameError():
    def __init__(self, account_name):
        self.account_name = account_name

    def __str__(self):
        return 'The username type has to be a string'


class UsernameIsTooLongError(Exception):
    def __init__(self, account_name):
        self.account_name = account_name

    def __str__(self):
        return 'The username ''{}'' has to be 25 chars or less.'.format(self.account_name)


def test_message_presence(account_name='guest'):
    if not isinstance(account_name, str):
        raise TypeOfUsernameError
    elif len(account_name) > 25:
        raise UsernameIsTooLongError(account_name)


def send_message(client_socket, message_to_send):
    message_in_json = json.dumps(message_to_send)
    message_in_binary = message_in_json('utf-8')
    client_socket.send(message_in_binary)

def receive_message(client_socket):
    message_in_binary = client_socket.recv(1024)
    message_in_string = message_in_binary.decode('utf-8')
    message_in_json = json.loads(message_in_string)
    # print("Received JIM message: {}".format(message_in_json))
    return message_in_json

def main():
    # action = Action()
    # print(action.presence)

    client = socket(AF_INET, SOCK_STREAM)
    server_address = 'localhost'
    server_port = '7777'
    mode = 'read'

    action = Action()

    test_message_presence(action.presence['user']['account_name'])
    action.presence['time'] = str(time.time())

    client.connect((server_address, server_port))

    send_message(client, action.presence)

    received_message = receive_message(client)

    if received_message['responce'] == 200:
        if mode == 'read':
            while True:
                print('Reading...')
                received_message = receive_message(client)
                print(received_message)
        elif mode == 'write':
            while True:
                print('Writing...')
                sending_message = input('==> ')

                action.msg['time'] = str(time.time())
                action.msg['to'] = '#all'
                action.msg['from'] = 'guest'
                action.msg['message'] = sending_message

                send_message(client, action.msg)

    client.close()



if __name__ == '__main__':
    main()
