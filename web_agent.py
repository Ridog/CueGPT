import Globals
import socket

def send_command(command):
    # Create a UDP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set the IP address and port number of the server
    server_address = (Globals.cueserver_ip, 52737)

    # Encode the command string as bytes and send it to the server
    message = command.encode()
    client_socket.sendto(message, server_address)

    # Close the socket
    client_socket.close()