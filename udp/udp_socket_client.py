import os
import socket

from udp.udp_socket_server import SERVER, PORT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "file_client.txt")


def client_udp():
    """
    Cliente socket UDP
    :return:
    """
    # Criando o socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Criando uma tupla com os valores do servidor e da porta
    server_address = (SERVER, PORT)
    print('++++++++++ Conectando a {} pela porta {} ++++++++++'.format(*server_address))

    try:
        # Abrindo o arquivo
        with open(FILENAME, "rb") as arq:
            while True:
                # Lendo o arquivo
                datafile = arq.read(1024)
                print('Enviando o arquivo {}'.format(FILENAME))
                # Enquanto o arquivo não for completamente enviado continua o envio
                while datafile:
                    # Enviando o arquivo para o servidor
                    sock.sendto(datafile, server_address)
                    datafile = arq.read(1024)
                else:
                    break
    finally:
        print('------------- Fechando conexão socket -------------')
        sock.close()


if __name__ == "__main__":
    client_udp()
