import time
import threading

def downLoad(filename,seconds):
    n = seconds
    print("开始下载:%s"%filename)
    while n>0:
        print("\r下载中。。。%s[%d/%d]"%(filename,seconds+1-n,seconds))
        time.sleep(0.5)
        n-=1
    print("下载完毕:%s"%filename)


# downLoad("QQ",12)
# downLoad("WX",18)

#换用多线程的调用方式，第一种
t1 = threading.Thread(target=downLoad,args=("QQ",12))
t1.setDaemon(True)
t2 = threading.Thread(target=downLoad,args=("WeiXin",15))

t1.start()
t2.start()

t2.join()
print('主线程结束')
# import os
#
# PI = 3.1416
#
# def rad(x):
#     '''
#     角度转弧度
#     :param x:角度
#     :return: 弧度
#     '''
#     return x * PI / 180
#
# #print(dir())
#
# if os.name == "nt":
#     os.system("dir")
# if os.name == "posix":
#     os.system("ls")

