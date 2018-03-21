import socket

from udp.udp_socket_server import SERVER, PORT

FILENAME = "file_origin.txt"


def client_tcp():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect the socket to the port where the server is listening
    server_address = (SERVER, PORT)
    print('++++++++++ Conectando a {} pela porta {} ++++++++++'.format(*server_address))

    try:
        # Send data
        with open(FILENAME, "rb") as arq:
            while True:
                datafile = arq.read(1024)
                print('Enviando o arquivo {}'.format(FILENAME))
                while datafile:
                    sock.sendto(datafile, server_address)
                    datafile = arq.read(1024)
                else:
                    break
    finally:
        print('------------- Fechando conexão socket -------------')
        sock.close()


if __name__ == "__main__":
    client_tcp()
