import socket
import threading

HOST = '127.0.0.1'
PORT = 8888

def handle_client(client_socket):
    try:
        request = client_socket.recv(4096)
        if not request:
            print("Empty request received.")
            client_socket.close()
            return

        request_lines = request.split(b'\n')
        first_line = request_lines[0].decode()

        if len(first_line.split(' ')) < 2:
            print("Malformed request line:", first_line)
            client_socket.close()
            return

        url = first_line.split(' ')[1]

        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]

        port_pos = temp.find(":")
        server_pos = temp.find("/")
        if server_pos == -1:
            server_pos = len(temp)

        server_host = ""
        server_port = -1
        if port_pos == -1 or server_pos < port_pos:
            server_port = 80
            server_host = temp[:server_pos]
        else:
            server_port = int(temp[(port_pos + 1):server_pos])
            server_host = temp[:port_pos]

        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((server_host, server_port))
            server_socket.send(request)

            while True:
                response = server_socket.recv(4096)
                if len(response) > 0:
                    client_socket.send(response)
                else:
                    break

            server_socket.close()
        except socket.error as e:
            print(f"Error connecting to server: {e}")

        client_socket.close()
    except Exception as e:
        print(f"Error handling client request: {e}")
        client_socket.close()

def start_proxy():
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.bind((HOST, PORT))
    proxy_socket.listen(5)
    print(f"[*] Proxy server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = proxy_socket.accept()
        print(f"[+] Received connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_proxy()
