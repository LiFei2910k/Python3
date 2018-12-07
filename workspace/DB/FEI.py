o = 35

def fn(x):
    global o
    o = ord(x)
    print(o)
    if 65 <= o <= 90:
        n = 45
        return "大写"
    else:
        return "不是大写"

print(fn("K"))
print(o) 