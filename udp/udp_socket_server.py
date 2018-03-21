import os
import socket

SERVER = socket.gethostname()
PORT = 10000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DESTINO = os.path.join(BASE_DIR, "deletavel_file_server.txt")


def server_udp():
    """
    Servidor socket UDP
    :return:
    """
    # Criando a socket UDP, através da constante socket.SOCK_DGRAM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Criando uma tupla com os valores do servidor e da porta
    server_address = (SERVER, PORT)
    print('Iniciando Servidor em {} na porta {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        # Esperando uma conexão
        print('+++++++++ Esperando por conexão +++++++++')
        try:
            while True:
                data, client = sock.recvfrom(1024)
                if data:
                    print('+++++++++ Recebendo arquivo do cliente {!r} +++++++++'.format(client))
                    with open(ARQUIVO_DESTINO, "wb") as arq:
                        arq.write(data)
        finally:
            # Fechando a conexão
            print("----------------- Finalizando conexão -----------------")
            sock.close()


if __name__ == "__main__":
    server_udp()
