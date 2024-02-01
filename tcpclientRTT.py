import socket
import time
import struct
print("We're in tcp client...");
#the server name and port client wishes to access
server_name = '16.171.233.204'
#'52.205.252.164'
server_port = 12000
#create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Set up a TCP connection with the server
#connection_socket will be assigned to this client on the server side
client_socket.connect((server_name, server_port))
msg = struct.pack('!I', 1); # 32 bit unsigned integer
# msg = "1"
sum = 0

for i in range(1,501):
    print("start of loop")
    start = time.time()
    #send the message to the TCP server
    client_socket.send(msg)
    print("sending message")
    #return values from the server
    response = client_socket.recv(1024)
    print("recieving message")
    end = time.time()
    time.sleep(0)
    sum = sum + (end-start)
    avg_RTT = sum/i
    print("running avg RTT = " + str(avg_RTT))
# print(msg.decode())
avg_RTT = sum/500
print("final avg RTT = " + str(avg_RTT))
client_socket.close()