#!/usr/bin/python
# -*-coding:utf-8 -*-
import urllib
import urllib.request
import re


#pattern=re.compile('\"(http\:\/\/[^http].*?\.(?:rar|zip))\"',re.M|re.I)

domain="http://www.html5tricks.com"
#pattern=re.compile('\/download.*?\.(?:rar|zip)',re.M|re.I)
pattern=re.compile('download\"\shref=\".*?\.(?:rar|zip)',re.M|re.I)

for i in range(11,12):
    try:
        jsonString=urllib.request.urlopen("http://www.html5tricks.com/category/html5-demo/page/"+str(i)).read().decode("utf-8")
        list=re.findall(pattern,jsonString)
        print(i)
        #print(list)
        #print(list[0][16:])
        for file in list:
        #for file in []:
            try:
                #download
                filename=file.split("/")[-1]
                #urllib.request.urlretrieve(domain+file,filename)
                urllib.request.urlretrieve(file[16:],filename)
                #log -> filename
                print(filename)
            except:
                print("下载文件异常："+str(i)+file)
                continue

    except:
            print("打开网页异常："+str(i)+file)
            continue
print("done-----")
				