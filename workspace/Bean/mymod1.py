import time

# 当此模块作为程序入口时(模块名为"__main__时可以使用")
if __name__ == "__main__":
    def getNumbers(a):
        a += "#"
        r = list()
        innumber = False
        iBegin = 0
        for i in range(len(a)):
            ch = a[i]
            if 48 <= ord(ch) <= 57:
                if not innumber:
                    innumber = True
                    iBegin = i
            else:
                if innumber:
                    innumber = False
                    r.append(a[iBegin:i])
            pass
        return tuple(r)

    print(time.time())
    a = "abc123dx5op0"
    print(getNumbers(a))
    print(time.time())

    print(__name__)