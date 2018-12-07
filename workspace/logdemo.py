import logging
import random

#基本配置，每个程序智能配置一次，运行时不可更改
#制定方式:文件、网络… 和日志格式
logging.basicConfig(
    filename = "log/demo.log",
    level = logging.DEBUG,
    format = "%(asctime)s|%(levelname)s|%(message)s",

)

try:
    for i in range(10):
        k = random.randint(0,100)
        print(k)
        logging.debug("恭喜你，生成了随机数:%d"%k)
except TypeError as e:
    logging.error("程序运行发生异常",e)