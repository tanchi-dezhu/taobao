import json
import time, random, requests
import datetime, hashlib

# 获得当前时间
now = datetime.datetime.now()
# 转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    id_list = ["your zhuoyi id1", "your zhuoyi id2", "your zhuoyi id3"]
    for id in id_list:
        # 获取微信openid
        num = random.randint(22000, 28000)  # 设置随机步数范围
        timestamp = int(time.time())
        # timestamp = 1568705432
        salt = '8061FD'
        url = 'http://weixin.droi.com/health/phone/index.php/SendWechat/getWxOpenid'
        sign = hashlib.md5((id + salt + str(timestamp)).encode("utf8")).hexdigest()
        data = {
            "accountId": id,
            "timeStamp": timestamp,
            "sign": sign,
        }
        print('------------------------------------------------------------')
        print("openidReqJson--->  " + json.dumps(data))
        r = requests.post(url, data=data)
        print("openidResJson--->  " + r.text.encode('utf-8').decode('unicode_escape'))
        res = json.loads(r.text.encode('utf-8').decode("unicode_escape"))
        openid = res.get("openid")
        # 刷步数
        url = "http://weixin.droi.com/health/phone/index.php/SendWechat/stepSubmit";
        sign = hashlib.md5((id + salt + str(num) + salt + str(timestamp) + salt + openid).encode("utf8")).hexdigest()
        data = {
            "accountId": id,
            "jibuNuber": num,
            "timeStamp": timestamp,
            "sign": sign,
        }
        print("fakeStepsReqJson--->  " + json.dumps(data))
        r = requests.post(url, data=data)
        print("fakeStepsResJson--->  " + r.text.encode('utf-8').decode('unicode_escape'))
        print(otherStyleTime)
        print('------------------------------------------------------------')
        print('')
