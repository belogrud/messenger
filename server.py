from socket import socket, AF_INET, SOCK_STREAM
import time
import json
import select

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


def receive_message(client_socket):
    message_in_binary = client_socket.recv(1024)
    message_in_string = message_in_binary.decode('utf-8')
    message_in_json = json.loads(message_in_string)
    # print("Received JIM message: {}".format(message_in_json))
    return message_in_json


def send_message(client_socket, message_to_send):
    message_in_json = json.dumps(message_to_send)
    message_in_binary = message_in_json.encode('utf-8')
    client_socket.send(message_in_binary)


def read_requests(r_clients, all_clients):
    """
    Чтение сообщений, которые будут посылать клиенты
    :param r_clients: клиенты которые могут отправлять сообщения
    :param all_clients: все клиенты
    :return:
    """
    # Список входящих сообщений
    messages = []

    for sock in r_clients:
        try:
            # Получаем входящие сообщения
            message = receive_message(sock)
            # Добавляем их в список
            # В идеале нам нужно сделать еще проверку, что сообщение нужного формата прежде чем его пересылать!
            # Пока оставим как есть, этим займемся позже
            messages.append(message)
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    # Возвращаем словарь сообщений
    return messages


def write_responses(messages, w_clients, all_clients):
    """
    Отправка сообщений тем клиентам, которые их ждут
    :param messages: список сообщений
    :param w_clients: клиенты которые читают
    :param all_clients: все клиенты
    :return:
    """

    for sock in w_clients:
        # Будем отправлять каждое сообщение всем
        for message in messages:
            try:
                # Отправить на тот сокет, который ожидает отправки
                # print('Заходит')
                send_message(sock, message)
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


if __name__ == '__main__':

    # response = Response()
    # print(response.ok)
    # print('Server ready.')

    server_address = ''
    server_port = 7777

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((server_address, server_port))
    server.listen(15)
    server.settimeout(0.2)

    clients = []
    addr = ''

    while True:
        try:
            client, client_address = server.accept()

            response = Response()
            response.ok['time'] = str(time.time())
            message_in_json = json.dumps(response.ok)
            message_in_binary = message_in_json.encode('utf-8')

            client.send(message_in_binary)
        except OSError as e:
            pass
        else:
            print('Was received request to connect from {}'.format(client_address))
            clients.append(client)
        finally:
            wait = 0
            r = []
            w = []
            try:
                r, w, e, = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)
            write_responses(requests, w, clients)

    client.close()

