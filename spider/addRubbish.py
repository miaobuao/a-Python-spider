import requests, sys, re, bs4, threading

def reencode(res):
    return res.text.encode(res.encoding).decode("utf8")

def getTagName(tagSet):
    namelist = []
    for x in range(0,len(tagSet)):
        tag = tagSet[x]
        name = tag.attrs.get("name")
        if not name == None:
            namelist.append(name)
    return namelist

def makedic(list):
    dic = {}
    for index in list:
        dic[index] = "1231223123"
    return dic

def makedata(url):
    res = requests.get(url)
    content = reencode(res)
    consecutiveContent = re.sub("\s", "", content)
    inputlist = bs4.BeautifulSoup(content,"html.parser").form.find_all("input")
    data = makedic(getTagName(inputlist))
    return data

class main(threading.Thread):
    def __init__(self,url, data, headers, threadName):
        threading.Thread.__init__(self)
        self.url = url
        self.data = data
        self.headers=headers
        self.threadName = threadName

    def run(self):
        while 1:
            r = requests.post(self.url,data=self.data, headers=self.headers)
            #print("["+self.threadName + "] : " + reencode(r))
            print(r.status_code)


headers = {
    "Proxy-Connection": "keep-alive",
    "Pragma": "no-cache",
    "Connection":"keep-alive",
    "Content-Type":"application/x-www-form-urlencoded",
    "X-Requested-With":"XMLHttpRequest"
}

#url = "http://www.vantic.cn/yug.asp"
#url2 = "http://cbb7.hkg.bcebos.com/index.html"
url = input("site address of form you need to analyze: ")
data = makedata(url)
url_send = input("the address you want to post data: ")
thread_count = input("count of threads you want to start: ")
for x in range(0,int(thread_count)):
    main(url_send, data, headers, str(x)).start()
    print("run" + str(x))