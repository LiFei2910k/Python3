from socket import *
from threading import Thread
import time
#from message import msg_encode
# 使用mysql数据库
import pymysql

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

all_clients = list()


# 服务器对客户端服务的线程
def rf(c, ad, conn):
    global all_clients
    while True:
        # 用st来表示要发送的消息内容
        st = None
        # 接收消息并解码
        bt = c.recv(1)
        if bt[0] == 2:
            bt = c.recv(1)
            print('找到消息头02')
            if bt[0] == 3:
                print('找到消息头03')
                # 读消息的长度
                bt = c.recv(2)
                l = bt[0]*16 + bt[1]//4
                print('消息长度:',l)
                # 根据长度读字节数
                bt = c.recv(l)
                # 对内容进行解码
                s = bt.decode()
                # 构造要发送的消息,添加发送者地址
                st = '%s:%s' % (ad, s)
            else:
                continue
        else:
            continue
        print(st)
        # 得到客户端发送来的消息,写入数据库
        # 获取游标
        cur = conn.cursor()
        # 执行sql语句
        sql = '''insert into msgs(addr,content)values('(%s,%s)','%s')'''%(ad[0],ad[1],s)
        cur.execute(sql)
        # 提交事务
        conn.commit()
        # 关闭游标
        cur.close()

        # 广播给所有的客户端
        for _c in all_clients:
            try:
                _c.sendall(msg_encode(st))
            except Exception as e:
                # 有异常,处理掉该客户端
                print('错误:', e)
                all_clients.remove(_c)
        time.sleep(1)


server = socket(AF_INET,
                SOCK_STREAM)
conn = pymysql.connect(
    host="www.laochu.net",
    port=3306,
    user="dba",
    passwd="***dk",
    db="zkdb",
    charset="utf8"
)
addr = ('0.0.0.0', 4008)
server.bind(addr)
server.listen()
print('服务启动 @ port:4008')

while True:
    client, caddr = server.accept()
    print('客户端连接:', caddr)
    all_clients.append(client)
    t = Thread(target=rf, args=(client, caddr, conn))
    t.setDaemon(True)
    t.start()

