import requests
import datetime
import logging


def getIpFromFile(filepath):
    try:
        with open(filepath, "r", encoding="utf8") as f:
            data = f.readline()
            return data.strip()
    except Exception as e:
        pass
    return ""

def wirteIpToFile(filepath, ip):
    try:
        with open(filepath, "w", encoding="utf8") as f:
            f.write(ip)
    except Exception as e:
        pass
    
def appendInfoToFile(filepath, ip, expire):
    with open(filepath, "a", encoding="utf8") as f: 
        f.write("%s\n" % datetime.datetime.now())   
        f.write("%s\n" % ip)   
        f.write("%s\n" % expire)   
    
def getIp():
    res = requests.get("http://members.3322.org/dyndns/getip")
    ip = res.text.strip()
    return ip

def requestSppedTest():

    req = requests.get("https://tisu-api.speedtest.cn/api/v2/speedup/reopen?source=www")
    # req.data
    rs = req.json()
    # {'code': 0, 'msg': 'ok', 'data': {'addr': 'X.X.X.X:25802', 'time': '2022-05-24 13:56:13', 'buid': 'XXX'}, 'errors': None}
    # {'code': 10002, 'msg': '您的操作太频繁', 'data': None, 'errors': None}
    if rs['code'] == 0 or rs['code'] == 10002:
        # 成功
        req = requests.get("https://tisu-api.speedtest.cn/api/v2/speedup/query?source=www-index")
        
        rs = req.json()
        if rs['code'] == 0:
            
            down_expire = rs['data']['down_expire']
            print(down_expire)
            return down_expire
    return ""

if __name__ == "__main__":
    localfile_path = "/home/pi/speedtest.txt"
    localfile_detail = "/home/pi/speedtest_detail.txt"
    old_ip = getIpFromFile(localfile_path)
    ip = getIp()
    if ip != old_ip:
        print("need update speedtest: %s, from %s" % (ip, old_ip))
        try:
            exptime = requestSppedTest()
            if exptime:
                appendInfoToFile(localfile_detail, ip, exptime)
                wirteIpToFile(localfile_path, ip)
        except Exception as e:
            logging.exception("")
            



