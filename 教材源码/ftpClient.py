import socket
import sys
import re
import struct
import getpass

def main(serverIP):
    # 创建Socket，连接服务器指定端口
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverIP, 10800))
    
    userId = input('请输入用户名：')
    # 使用getpass模块的getpass()方法获取密码，不回显
    userPwd = getpass.getpass('请输入密码：')
    message = userId+','+userPwd
    # 尝试登录
    sock.send(message.encode())
    login = sock.recv(100)
    # 验证是否登录成功
    if login == b'error':
        print('用户名或密码错误')
        return
    
    # 整数编码大小
    intSize = struct.calcsize('I')
    
    while True:
        # 接收客户端命令，其中##>是提示符
        command = input('##> ').lower().strip()
        # 如果没有输入任何有效字符
        # 提前进入下一次循环，等待用户继续输入
        if not command:
            continue
        
        # 向服务端发送命令
        command = ' '.join(command.split())
        sock.send(command.encode())
        
        # 退出
        if command in ('quit', 'q'):
            break
        
        # 查看文件列表
        elif command in ('list', 'ls', 'dir'):
            loc_size = struct.unpack('I', sock.recv(intSize))[0]
            files = eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
                
        # 切换至上一级目录
        elif ''.join(command.split()) == 'cd..':
            print(sock.recv(100).decode())
            
        # 查看当前工作目录
        elif command in ('cwd', 'cd'):
            print(sock.recv(1024).decode())
            
        # 切换至指定文件夹
        elif command.startswith('cd '):
            print(sock.recv(100).decode())
            
        # 从服务器下载文件
        elif command.startswith('get '):
            isFileExist = sock.recv(2)
            # 文件不存在
            if isFileExist != b'ok':
                print('error')
                
            # 文件存在，开始下载
            else:
                print('downloading.', end='')
                size = struct.unpack('I', sock.recv(intSize))[0]
                # 接收文件数据
                data = b''
                while True:
                    if size == 0:
                        break
                    elif size > 4096:
                        temp = sock.recv(4096)
                        data += temp
                        size -= len(temp)
                    else:
                        temp = sock.recv(size)
                        data += temp
                        size -= len(temp)
                # 接收完成后写入本地文件
                with open(command.split()[1], 'wb') as fp:
                    fp.write(data)
                print('ok')
                
        # 无效命令
        else:
            print('无效命令')
    sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:{0} serverIPAddress'.format(sys.argv[0]))
        exit()
        
    serverIP = sys.argv[1]
    if re.match(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', serverIP):
        main(serverIP)
    else:
        print('服务器地址不合法')
        exit()
