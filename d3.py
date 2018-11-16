#coding = utf8
from logInit import *
null="null"
import requests,random,copy,time



# !/usr/bin/env python
# -*- coding:utf-8 -*-



# with open('egg2.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, dialect='excel')
#     spamwriter.writerow(['a', '1', '1', '2', '2'])
#     spamwriter.writerow(['b', '3', '3', '6', '4'])
#     spamwriter.writerow(['c', '7', '7', '10', '4'])
#     spamwriter.writerow(['d', '11', '11', '11', '1'])
#     spamwriter.writerow(['e', '12', '12', '14', '3'])


class apiTest(object):
    def __init__(self):
        self.data = {
			"id": "a26d4483-9ee8-a2c5-939b-08c6f2d606e8",
			"headers": "Accept: application/json, text/plain, */*\nOrigin: http://test-ijx.hfjy.com\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36\nContent-Type: application/x-www-form-urlencoded\nReferer: http://test-ijx.hfjy.com/F_ijx/?_0.6654825350535827\nAccept-Encoding: gzip, deflate\nAccept-Language: zh-CN,zh;q=0.8\nCookie: UUID=Cm9mhFvJl6KYi3CjDbijAg==; _ga=GA1.2.1370017300.1541062356; cn_4a16b28a400d8g0d3e30_dplus=%7B%22distinct_id%22%3A%20%2216699c52f50b64-06283e672882aa-36624308-1fa400-16699c52f51b8f%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201541064330%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201541064330%7D%2C%22initial_view_time%22%3A%20%221541060596%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fwww.hfjy.com%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.hfjy.com%22%7D; UM_distinctid=16699c52f50b64-06283e672882aa-36624308-1fa400-16699c52f51b8f; pt_68d72831=uid=neXC3VwBavKYtJVz0HXNFA&nid=0&vid=TCdCH/s5ukhL8lf2AfrG3Q&vn=8&pvn=1&sact=1541143216106&to_flag=0&pl=VaphPVOYPXToJEcKE2kbNw*pt*1541143216106; pt_s_68d72831=vt=1541143216106&cad=; MSVCSESSION=2d173af45bdfecb034472072461261b834468\n",
			# "url": "http://test-ijx.hfjy.com/education/passport/login",
            "url": "http://test-ijx.hfjy.com/education/foreign/entry/saveImg",
			"pathVariables": {},
			"preRequestScript": null,
			"method": "POST",
			"collectionId": "5c165af5-a1ce-7acf-8905-d5b8c1d787cc",
			"data": [
				{
					"key": "teacherId",
					"value": "22171"
				},
				{
					"key": "sign",
					"value": "443ff71807d0b06d2b0874fbaa58b82c"
				},
                {
                    "key": "info",
                    "value": '['
                  '{"type":"1","url":"http://img.wzzsl.com/10847934065bd29f4a5857c8.06839768.png"},'
                  '{"type":"1","url":"http://img.wzzsl.com/16734222245bd29d215f7572.19250681.png"},'
                  '{"type":"2","url":"http://img.wzzsl.com/10847934065bd29f4a5857c8.06839768.png"},'
                  '{"type":"2","url":"http://img.wzzsl.com/10847934065bd29f4a5857c8.06839768.png"},'
                  '{"type":"3","url":"http://img.wzzsl.com/470392225bd29c92754d17.66389654.png"},'
                  '{"type":"3","url":"http://img.wzzsl.com/470392225bd29c92754d17.66389654.png"},'
                  '{"type":"5","url":"http://img.wzzsl.com/3699797615bd29da60f2244.43296795.png"},'
                  '{"type":"5","url":"http://img.wzzsl.com/470392225bd29c92754d17.66389654.png"},'
                  '{"type":"6","url":"http://img.wzzsl.com/3699797615bd29da60f2244.43296795.png"},'
                  '{"type":"6","url":"http://img.wzzsl.com/3699797615bd29da60f2244.43296795.png"},'
                  '{"type":"7","url":"http://img.wzzsl.com/3699797615bd29da60f2244.43296795.png"},'
                  '{"type":"8","url":"http://img.wzzsl.com/16734222245bd29d215f7572.19250681.png"},'
                  '{"type":"4","url":"http://img.wzzsl.com/16734222245bd29d215f7572.19250681.png"},'
                  '{"type":"4","url":"http://img.wzzsl.com/16734222245bd29d215f7572.19250681.png"}]'
                }
			],
			"dataMode": "urlencoded",
			"name": "http://test-ijx.hfjy.com/education/foreign/entry/saveImg",
			"description": "",
			"descriptionFormat": "html",
			"time": 1541405708551,
			"version": 2,
			"responses": [],
			"tests": null,
			"currentHelper": "normal",
			"helperAttributes": {}
		}
        self.min = 5
        self.max = 10000




    def recordResults(self,data):
        with open("data.txt","a",encoding='utf8') as file:
            file.write("%s \n"%(data))
        logging.info("%s \n"%(data))

    def soloRequest(self,body):
        error_list = ["error","Error","False","false","失败","错误","异常","禁止"]
        time.sleep(1)
        # with requests.request(method=self.method, url=self.url, params=body) as response:
        with requests.request(method=self.method,url=self.url,data=body) as response :
            state = False
            for error in error_list:
                if error in response.text:
                        return False,response.text
            return True,response.text
    def specifyLength(self,spec_num=False):
        if not spec_num:
            low = self.min
            height = self.max
            mid =  int((low + height) / 2)
            # str(random.randint(10 ** mid, 10 ** (mid + 1)))
            # return int((low + height) / 2)
            return str(random.randint(10 ** mid, 10 ** (mid + 1)))
        else:
            return str(random.randint(10 ** spec_num, 10 ** (spec_num + 1)))

    def limitCheck(self,body,key):
        temp = copy.copy(body)
        temp[key] = self.specifyLength(spec_num=100000)  # 7924 7924
        spec_response = self.soloRequest(temp)

        self.min = 1
        self.max = 100000

        while abs(self.min - self.max) > 1:
            temp_len = int((self.min + self.max) / 2)
            temp[key] = self.specifyLength()
            response = self.soloRequest(temp)
            logging.debug("key:%s max:%s min:%s cur:%s response:%s"%(key,str(self.max),str(self.min),str(temp_len),response))
            if response == spec_response:
                self.max = temp_len
            else:
                self.min = temp_len
        for i in range(self.max + 1, self.min - 2, -1):
            temp[key] = self.specifyLength(spec_num=i)
            response = self.soloRequest(temp)
            logging.debug("finish check:%s response:%s"%(str(len(temp[key])),response))
            if response != spec_response:
                self.recordResults("%s %s:limit:%s \n" % (self.name, str(key), str(len(temp[key]))))
                return i
        return False

    def exceptionCheck(self,body,key):
        temp = copy.copy(body)
        temp[key] = ""
        spec_response = self.soloRequest(temp)
        self.recordResults("%s exceptionCheck: %s为空 response:%s"%(self.name,key,spec_response))
        temp.pop(key)
        spec_response = self.soloRequest(temp)
        self.recordResults("%s exceptionCheck: %s不传 response:%s" % (self.name,key, spec_response))

    def dataReduction(self,data):
        self.headers = data["headers"]
        self.url = data["url"]
        self.method = data["method"]
        self.name = data["url"]
        body = {}
        for solo_data in data["data"]:
            body[solo_data["key"]]=solo_data["value"]
        for key in body:
            self.exceptionCheck(body,key)
            for solo in range(3):
                limit = self.limitCheck(body,key)
                if limit:
                    break

if __name__ == '__main__':
    test = apiTest()
    # print (test.data)
    # print (test.dataReduction(test.data))
    # test.getData(".\\postmandata\\ijx.json.postman_collection")
