from urllib import request,parse
import json



def downPic(url,fn):
    resp = request.urlopen(url)
    b = resp.read()
    #b.decode()
    fn = "pics/%s.jpg"%fn
    f = open(fn, "bw")
    f.write(b)
    f.close()

def getImgUrls(kw,pn):
    result = list()
    params = {"tn": "resultjson_com",
              "ipn": "rj",
              "ct": "201326592",
              "fp": "result",
              "queryWord": kw,
              "cl": "2",
              "lm": "-1",
              "ie": "utf-8",
              "oe": "utf-8",
              "st": "-1",
              "z": "0",
              "ic": "0",
              "hd": "0",
              "latest": "0",
              "copyright": "0",
              "face": "0",
              "istype": "2",
              "nc": "1",
              "pn": pn,
              "rn": "30",
              "gsm": "10e",
              "word": kw,
              }
    urlpara = parse.urlencode(params)
    resp = request.urlopen(url + "?" + urlpara)
    jo = json.loads(s)
    dt = jo.get("data")
    for i in dt:
        img = i.get("thumbURL")
        if img:
            result.append(img)
        return result



kw = "金庸"
url = "https://image.baidu.com/search/acjson"
k = 0

for page in range(1,6):
    r = getImgUrls(kw, page*30)
    for u in r:
        downPic(u, "pic%d" % k)
        k += 1


