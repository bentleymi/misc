#usage:  Open a python shell with "python [enter]", update the server_address on line 6 below and then copy and paste into your python shell

import socket

# Define the server address and port
server_address = ('localhost', 9514)
count = 1000

i=0
while i<count:
 #  Create a UDP socket
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 message=b'Test message for UDP'
 print(f'Sending: {message}')
 sock.sendto(message, server_address)
 i+=1
