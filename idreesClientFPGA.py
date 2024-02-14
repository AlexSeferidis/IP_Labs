import socket
import time
import select
import subprocess
import re

NIOS_CMD_SHELL_BAT = "C:/intelFPGA_lite/18.1/nios2eds/Nios II Command Shell.bat"

def send_tcp_server(cmd):
    print("Sending message to server")
    server_name = '16.171.144.67'
    server_port = 12000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    print("Sending message to server")
    send_time = time.time()
    try:
        client_socket.send(cmd.encode())
    except socket.error:
        print("Error sending message to server")
        return
    ready_to_read, _, _ = select.select([client_socket], [], [], 1.0)  # Timeout of 1 second

    if ready_to_read:
        print("Waiting for server response")
        modified_msg = client_socket.recv(1024)
        receive_time = time.time()
        print("RTT: ", receive_time - send_time)
    else:
        print("Timeout waiting for server response")

    client_socket.close()
    return modified_msg

def parse_output(output):
    # Use regular expressions to find content between <--> tags
    matches = re.findall(r'<-->(.*?)<-->', output, re.DOTALL)
    return matches

def handle_jtag(cmd):
    # check if at least one character is being sent down
    assert len(cmd) >= 1, "Please make the cmd a single character"

    # create a subprocess which will run the nios2-terminal
    process = subprocess.Popen(
        NIOS_CMD_SHELL_BAT,
        bufsize=0,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    # send the cmd string to the nios2-terminal, read the output and terminate the process
    print("Testing the nios2-terminal")
    try:
        vals, err = process.communicate(
            bytes("nios2-terminal <<< {}".format(cmd), "utf-8")
        )
        process.terminate()
        parsed_content = parse_output(vals.decode("utf-8"))

        # Print the extracted content
        for content in parsed_content:
            print("Parsed Content:", content)

        return parsed_content  # Return the parsed content to be sent to the server

    except subprocess.TimeoutExpired:
        vals = "Failed"
        process.terminate()

    return vals

def main():
    res = handle_jtag("testing")
    print("Result", res)
    print(send_tcp_server(str(res)))  # Convert parsed content to string before sending to server

if __name__ == "__main__":
    main()
