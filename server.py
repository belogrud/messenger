from socket import *
# import time
import json

#   JIM definitions.
message_precense = {
    'action': 'presence'
}

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)

while True:
    client, addr = s.accept()

    message_in_json = json.dumps(message_precense)
    message_in_bynary = message_in_json.encode('utf-8')
    client.send(message_in_bynary)

    client.close()

