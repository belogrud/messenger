from socket import *
import json

#   JIM definitions.
message_presence = {
    'action': 'presence'
}

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))
message_in_binary = s.recv(1024)
s.close()

message_in_string = message_in_binary.decode('utf-8')
message_in_json = json.loads(message_in_string)
print("Json message {}".format(message_in_json))

# print("Текущее время: %s" % tm.decode('utf-8'))
# print("Текущее время: %s" % tm)

