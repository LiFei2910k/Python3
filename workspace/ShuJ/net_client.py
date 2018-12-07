import threading
import socket as sk
import time
#from message import msg_encode

def msg_encode(s):
    r = bytearray()
    b = s.encode("utf-8")
    l = len(b)
    r.append(2)
    r.append(3)
    # 把l拆分成两个不为02 03的字节
    r.append((l//64)<<2)
    r.append((l%64)<<2)
    for _ in b:
        r.append(_)
    return r

#创建socket,ipv4,tcp字节流
s = sk.socket(
    sk.AF_INET,
    sk.SOCK_STREAM
)


# 定义一个函数,循环接收消息并显示
def rcv():
    global s
    while True:
        # 接收消息并解码
        bt = s.recv(1)
        if bt[0] == 2:
            bt = s.recv(1)
            print('找到消息头02')
            if bt[0] == 3:
                print('找到消息头03')
                # 读消息的长度
                bt = s.recv(2)
                l = bt[0]*16 + bt[1]//4
                print('消息长度:',l)
                # 根据长度读字节数
                bt = s.recv(l)
                # 对内容进行解码
                msg = bt.decode()
                # 输出接收到的消息
                print('[RCV:]',msg)
            else:
                continue
        else:
            continue
        time.sleep(1)


# 提供一个地址,连接
addr =('172.16.0.124', 4008)
s.connect(addr)

# 创建一个线程并启动,开始接收数据
task = threading.Thread(target=rcv)
task.setDaemon(True)
task.start()

# 输入数据并发送
while True:
    txt = input()
    if txt == 'bye':
        break
    s.sendall(msg_encode(txt))
