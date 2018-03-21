import socket

SERVER = socket.gethostname()
PORT = 10000


def server_tcp():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = (SERVER, PORT)
    print('Iniciando Servidor em {} na porta {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        # Wait for a connection
        print('+++++++++ Esperando por conexão +++++++++')
        try:
            while True:
                data, cliente = sock.recvfrom(1024)
                if data:
                    print('+++++++++ Recebendo arquivo do cliente {!r} +++++++++'.format(cliente))
                    with open("received_file.txt", "wb") as arq:
                        arq.write(data)
        finally:
            # Clean up the connection
            print("----------------- Finalizando conexão -----------------")
            sock.close()


if __name__ == "__main__":
    server_tcp()
