#生产者-消费者模型
import threading
import time
import random


#包子
class Baozi():
	def __init__(self, count):
		super(Baozi, self).__init__()
		self.count = count
	def add(self,x):
		self.count += x
	def sub(self,x):
		self.count -= x

#以下为生产者和消费者，都继承了Thread类
#生产者
class Producer(threading.Thread):
	def __init__(self, cond, food):
		super(Producer, self).__init__()
		self.food = food #生产的商品为包子
		self.cond = cond #用于控制同步的条件
	def run(self):
		while True:
			time.sleep(5)#每13秒生产一次13个包子
			if food.count<=37:#如果当前数量不足则生产
				cond.acquire()
				food.add(13)
				cond.notifyAll()#通知等待的线程
				cond.release()
				print('生产完毕，数量：%d'%food.count)
			else:#当前数量超过限定值则暂停生产
				print('暂停生产，数量：%d'%food.count)

#消费者
class Consumer(threading.Thread):
	def __init__(self,num,cond,food):
		super(Consumer, self).__init__()
		self.cond = cond #同步条件
		self.food = food #消费的物品
		self.num = num #每次消费数量
	def run(self):
		while True:
			time.sleep(6) #每6秒消费一次
			cond.acquire() #请求锁
			x=random.randrange(4,10)#随机消费4-9个
			if food.count<x:
				print('消费者 %d 等待购买'%self.num)
				cond.wait()#如果库存不足则等待
			else:
				food.sub(x)
				print('消费者 %d 购买%d个完毕，剩余数量:%d'%(self.num,x,food.count))
			cond.release()#购买完毕则释放

#构造生产物品和同步条件
food=Baozi(0)
cond=threading.Condition()
#构造一个生产者，三个消费者
prd=Producer(cond,food)
csm1=Consumer(1,cond,food)
csm2=Consumer(2,cond,food)
csm3=Consumer(3,cond,food)
#启动线程
prd.start()
csm1.start()
csm2.start()
csm3.start()