import socket
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
                'account_name': 'username1',
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
            'to': 'account_name',
            'from': 'account_name',
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

def main():
    # action = Action()
    # print(action.presence)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 7777))
    message_in_binary = s.recv(1024)
    s.close()

    message_in_string = message_in_binary.decode('utf-8')
    message_in_json = json.loads(message_in_string)
    print("Received JIM message: {}".format(message_in_json))

if __name__ == '__main__':
    main()

