# -*-coding:utf-8 -*-
import re
import urllib.request
import pymysql

 
url = 'http://so.gushiwen.org/view_'  # 入口页面, 可以换成别的
cnt = 0
maxCnt=72845

conn = pymysql.connect(user='root', passwd='root', host='localhost', db='demo1',charset='utf8')
conn.encoding="utf-8"
cur = conn.cursor()

#conn.set_character_set('utf8')
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')

linkre = re.compile('son1[\s\S]+h1\>(.+?)\<[\s\S]+?(\<p[\s\S]+?)\<\/div',re.M|re.I)
while cnt<maxCnt:
  cnt=cnt+1;
  # 避免程序异常中止, 用try..catch处理异常
  try:
    print(cnt)
    data = urllib.request.urlopen(url+str(cnt)+".aspx").read().decode('utf-8')
     # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    da=linkre.findall(data)

    #print(da[0][0])
    #print(da[0][1])
    # print(da[0][0])

    if (da and len(da[0])) ==2:
        cur.execute("insert into tb2 (name,detail) values('%s', '%s')" % (da[0][0],da[0][1]))
        #cur.execute('insert into tb2 (name,detail) values("www","eeee")')
        conn.commit();

  except:
    print(str(cnt)+" 异常")
    continue
 
# print(cur.execute("select * from tb2 where id=12"))
cur.close()    
conn.close()
print(str(cnt)+" 完成！")
    