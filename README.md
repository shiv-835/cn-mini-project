# CN MINI PROJECT - Simple Proxy Server

## Submitted by
Shiv Chauhan 22BCS15180

## Overview

This Python-based proxy server listens for client requests and forwards them to the appropriate web server, relaying the responses back to the client. It supports basic HTTP requests and handles connections using threading for concurrent client handling.

## Features

- Listens for incoming client connections on a specified host and port.
- Forwards requests to the target server and returns the response.
- Supports multi-threading to handle multiple clients simultaneously.

## Requirements

- Python 3.x

## How to Run the Server

1. Clone the repository (if applicable):
   ```bash
   git clone https://github.com/shiv-835/cn-mini-project.git
   cd proxy-server
   ```

2. Run the server:
   ```bash
   python proxy_server.py
   ```

3. The server will start listening on `127.0.0.1:8888`.

## Usage

- Use any HTTP client (e.g., browser or Postman) to send requests to `http://127.0.0.1:8888/`.
- The server will handle the requests and forward them to the appropriate external server.

## Example

To test the proxy, you can use a browser to navigate to:
```
http://127.0.0.1:8888/http://example.com
```
The response from `example.com` will be displayed.

## Error Handling

The server includes basic error handling for malformed requests and connection issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Based on standard socket programming principles in Python.

---

Feel free to modify the repository link and other sections to fit your project's details!
