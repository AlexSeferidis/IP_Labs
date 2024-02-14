import socket
import select

print("TCP Server")

server_port = 12000
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcome_socket.bind(('0.0.0.0', server_port))
welcome_socket.listen(1)

print('Server running on port', server_port)

while True:
    connection_socket, _ = welcome_socket.accept()
    connection_socket.setblocking(0)  # Set socket to non-blocking mode

    ready_to_read, _, _ = select.select([connection_socket], [], [], 1.0)  # Timeout of 1 second

    if ready_to_read:
        cmsg = connection_socket.recv(1024)
        print("Received message from client:", cmsg.decode())

        # Send a response back to the client
        connection_socket.send("1".encode())
        connection_socket.close()
    else:
        print("Timeout waiting for client message")
