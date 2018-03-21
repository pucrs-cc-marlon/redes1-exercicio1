import socket

SERVER = socket.gethostname()
PORT = 10000


def server_tcp():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (SERVER, PORT)
    print('Iniciando Servidor em {} na porta {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('+++++++++ Esperando por conexão +++++++++')
        connection, client_address = sock.accept()
        try:
            print('+++++++++ Conectado por', client_address, "+++++++++")
            with open("received_file.txt", "wb") as arq:
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
            # Clean up the connection
            print("----------------- Finalizando conexão -----------------")
            connection.close()


if __name__ == "__main__":
    server_tcp()
