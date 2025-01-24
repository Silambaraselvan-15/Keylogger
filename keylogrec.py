import socket
server_address=('192.168.1.5',8000)
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
    server_socket.bind(server_address)
    server_socket.listen(1)

    while True:
        connection,client_address=server_socket.accept()
        with connection:
            while True:
                data=connection.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))