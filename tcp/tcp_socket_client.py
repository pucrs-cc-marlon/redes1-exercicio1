import os
import socket

from tcp.tcp_socket_server import SERVER, PORT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "file_client.txt")


def client_tcp():
    """
    Cliente de Socket TCP/IP
    :return:
    """
    # Criando o TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta o socket na porta e o endereço do servidor
    server_address = (SERVER, PORT)
    print('++++++++++ Conectando a {} pela porta {} ++++++++++'.format(*server_address))
    sock.connect(server_address)

    try:
        # Send data
        with open(FILENAME, "rb") as arq:
            while True:
                datafile = arq.read(1024)
                print('Enviando o arquivo {}'.format(FILENAME))
                while datafile:
                    sock.send(datafile)
                    datafile = arq.read(1024)
                    data = sock.recv(50)
                    if data:
                        print('Mensagem do Server {!r}'.format(data))
                else:
                    break
    finally:
        print('------------- Fechando conexão socket -------------')
        sock.close()


if __name__ == "__main__":
    client_tcp()
