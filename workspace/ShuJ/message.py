# 把消息字符串进行封装,成为字节数组
# 前2个字节为特定的消息头  02 03
# 接下来的两个字节为消息长度N
# 接下来的N个字节为消息utf8编码的字节

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
