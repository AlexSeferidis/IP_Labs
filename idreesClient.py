import socket
import time
import select

print("TCP Client")

server_name = '16.171.144.67'
server_port = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_name, server_port))

rtt = 0
for i in range(0, 499):
    print("Sending message to server")
    send_time = time.time()
    try:
        client_socket.send("1".encode())
    except socket.error as e:
        print("Error sending message to server: ", e)
        
        continue

    ready_to_read, _, _ = select.select([client_socket], [], [], 1.0)  # Timeout of 1 second

    if ready_to_read:
        print("Waiting for server response")
        modified_msg = client_socket.recv(1024)
        receive_time = time.time()
        rtt += receive_time - send_time
    else:
        print("Timeout waiting for server response")

client_socket.close()
print("Average RTT: ", rtt / 499)
