import csv,re
# import toolbox
from logInit import *
from apitest.parm import *
class Postman2Csv(object):
    def __init__(self,path,resultpath="..//data//temp.csv"):
        self.path = path
        self.resultpath = resultpath #结果路径
        self.header = csv_parm.CHINA_KEY #中文key
        self.key =  csv_parm.KEY #key
    def run(self):
        try:
            data = self.getData()
            self.write2Csv(data)
            log.logger.info("postman转csv成功:%s"%self.resultpath)
        except Exception as es:
            log.logger.error("postman转csv失败")
            log.logger.error(es)

    def csvWrite(self,data): #写单行
        with open(self.resultpath, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile,dialect='excel')
            spamwriter.writerow(data)

    def printCsv(self): #打印csv现有内容
        with open(self.path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))

    def write2Csv(self,data): #根据数据写入csv
        self.csvWrite(self.header)
        for solo_data in data:
            self.csvWrite([PostParm.START]) #START标志位
            self.csvWrite(self.key)     #英文标签
            self.csvWrite(solo_data)    #数据
            self.csvWrite([PostParm.END]) #END标志位

    def getData(self,Cookie=False): #从postman获取数据
        false = PostParm.FALSE    #初始化特殊字符
        true = PostParm.TRUE
        null = PostParm.NULL
        with open(self.path,"r") as file: #读取文件会获取dict格式
            data = file.read()
            data = eval(data)[PostParm.REQUESTS]
        all_data = []
        for solo_data in data: #便利数据
            url = solo_data[PostParm.URL]
            url_list  = url.split("?")[0].split("/") #拆解url 获取path路径list
            url_parm = ""
            if len(url)>1:   #包含? 增加 url params
                url_parm = url.split("?")[-1]
            url = url.split("?")[0] #去除?后内容
            error_headers = re.findall("\n//.*", solo_data[PostParm.HEADERS])  # //是为了处理postman 中被注释的数据
            if error_headers:
                for error_header in error_headers:
                    solo_data[PostParm.HEADERS] = solo_data[PostParm.HEADERS].replace(error_header, "")

            if not Cookie:  #不需要cookie
                cookies = re.findall("Cookie.*",solo_data[PostParm.HEADERS])  #正则并删除cookie
                if cookies:
                    for cookie in cookies:
                        solo_data[PostParm.HEADERS] = solo_data[PostParm.HEADERS].replace(cookie,"")
            #组装数据
            temp_list = ["", #lv
                         "", #Cname
                         url_list[-1], #name
                         solo_data[PostParm.NAME], #Describe
                         ".\\"+url_list[-2]+"\\"+url_list[-1],#ResualPath
                         solo_data[PostParm.METHOD],#method
                         url, #url
                         solo_data[PostParm.HEADERS],#headers
                         solo_data[PostParm.DATA],#data
                         solo_data[PostParm.DATATYPE],#datatype
                         url_parm,  # UrlParams
                         "" #TestType
                        ]
            all_data.append(temp_list)
        return all_data

class Csv2Dict(object):
    def __init__(self,path="..//data//temp.csv"):
        self.path = path
        self.key =  csv_parm.KEY #key
    def run(self):
        try:
            data = a.readAll()
            dict_data = a.list2Dict(data)
            logging.debug("CSV文件内容序列化成功:%s",str(dict_data))
            return dict_data
        except Exception as ex:
            logging.error("CSV文件内容序列化失败:%s", str(ex))
            return False

        print(dict_data)
    def readAll(self):
        temp_list = []
        with open(self.path, newline='') as csvfile:
            spamreader = csv.reader(csvfile,dialect='excel')
            for solo in spamreader:
                temp_list.append(solo)
        return temp_list
    def list2Dict(self,data):
        data_temp = []
        start_list = []
        for index,value in enumerate(data):
            if value == [PostParm.START]:
                start_list.append(index)
        for index in start_list:
            solo_data = {}
            for sub_index,key in enumerate(data[index+1]):
                solo_data[key] = data[index+2][sub_index]
            solo_data[csv_parm.HEADERS] = self.header2Dict(solo_data[csv_parm.HEADERS])
            data_temp.append(solo_data)
        return data_temp
    def header2Dict(self,header_string):
        while header_string[-1] == "\n":
            header_string =  header_string[:-1]
        header_string =  '\''+header_string+'\''
        header_string = header_string.replace("\n","\',\'")
        header_string = header_string.replace(":", "\':\'")
        header_string = header_string.replace("http\':\'//","http://")
        header_string = header_string.replace("https\':\'//", "https://")
        header_string = '{'+header_string+'}'
        header_dict = eval(header_string)
        return header_dict

if __name__ == '__main__':
    pass
    # test = Postman2Csv("..\\postmandata\\ijx.json.postman_collection")
    # test.run()
    #
    # a =  Csv2Dict()
    # a.run()


