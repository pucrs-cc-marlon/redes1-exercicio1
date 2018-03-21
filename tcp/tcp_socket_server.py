import os
import socket

SERVER = socket.gethostname()
PORT = 10000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DESTINO = os.path.join(BASE_DIR, "deletavel_file_server.txt")


def server_tcp():
    """
    Servidor socket TCP/IP
    :return: None
    """
    # Criando o socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta o socket na porta
    server_address = (SERVER, PORT)
    print('Iniciando Servidor em {} na porta {}'.format(*server_address))
    sock.bind(server_address)

    # Escuta as conexões recebidas
    sock.listen(1)

    while True:
        # Esperando as conexões
        print('+++++++++ Esperando por conexão +++++++++')
        connection, client_address = sock.accept()
        try:
            print('+++++++++ Conectado por', client_address, "+++++++++")
            with open(ARQUIVO_DESTINO, "wb") as arq:
                while True:
                    print('+++++++++ Recebendo o arquivo +++++++++')
                    data = connection.recv(1024)
                    if data:
                        # print('Respondendo para o cliente')
                        arq.write(data)
                        connection.sendall(b"+++++++++ Recebendo o arquivo +++++++++")
                    else:
                        print('Sem dados de', client_address)
                        break
        finally:
            # Fecha a conexão
            print("----------------- Finalizando conexão -----------------")
            connection.close()


if __name__ == "__main__":
    server_tcp()
