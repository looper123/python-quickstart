import socket


# 服务端
def first_socket_server():
    # 参数说明  参数1 套接字family 参数2 连接类型  面向无连接：socket_dgram  面向连接：socket_stream
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host_name = socket.gethostname()
    port = 9999
    # 绑定host 和端口
    server_socket.bind((host_name, port))
    # 设置最大连接数 超过后排队
    server_socket.listen(5)
    while True:
        print("socket server starting.......")
        # 当前服务如果没有客户端访问 执行到这一步停止(准备接收来自client的请求)
        client_socket, addr = server_socket.accept()
        print("连接地址：{address}".format(address=addr))


if __name__ == '__main__':
    first_socket_server()
