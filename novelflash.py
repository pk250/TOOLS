# -*-coding:utf8-*-

import requests
from lxml import html

def main():
    res=requests.get(u"https://www.biqudu.net/31_31729/",verify=False).text
    etree=html.etree
    s=etree.HTML(res)
    film=s.xpath('//*[@id="list"]/dl/dd[1]/a/@href')
    if len(film)==1:
         fileRead(film[0])
    return 1

def fileRead(res):
    try:
        f=open("data.csv","r")
        if f.read() == res:
            print "is equarts"
        else:
            f=open("data.csv","w")
            f.write(res)
            sendMessage()
    except :
        print u"文件不存在"
        f=open("data.csv","w")
        f.write(res)
    f.close()
    return 1

def sendMessage():
    requests.get("https://sc.ftqq.com/SCU8097Ta14e81296af67c8966034cbd71fbc054590b581505a80.send?text=小说更新啦&desp=元尊小说更新啦",verify=False)
    return 1

if __name__ =="__main__":
    main()
    print "novelflash run on 5s"