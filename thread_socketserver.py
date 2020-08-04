# 文件位置:/code/chapter2/section2/socket_server.py
# coding:utf-8
#!/usr/bin/python
import socket
import time
import threading

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello, world! <h1> from the5fire 《Django企业开发实战》</h1>\n'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sat, 10 jun 2017 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body)+16),
    body,
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    time.sleep(10)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()


def main():
    # socket.AF_INET    用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM    基于TCP的流式socket通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用，保证我们每次Ctrl C之后，快速再次重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8080))
    # 可参考：https://stackoverflow.com/questions/2444459/python-sock-listen
    serversocket.listen(10)
    serversocket.setblocking(1)
    print('http://127.0.0.1:8080')

    try:
        while True:
            conn, address = serversocket.accept()
            t = threading.Thread(target=handle_connection,args=(conn,address),name = 'one thread')
            t.start()
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()