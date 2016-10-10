#!/usr/bin/python
# -*-coding:utf-8 -*-
import urllib
import urllib.request
import re

pattern=re.compile('(http\:\/\/www\.htmleaf\.com\/(?:jQuery|html5|css3).*?\.html)\"\>',re.M|re.I)
pattern2=re.compile('http\:.*?\.(?:zip|rar)',re.M|re.I)
pagePattern=re.compile('(list\_\d+?\_\d+?)\.html',re.M|re.I)

src=["http://www.htmleaf.com/jQuery/pubuliuchajian/","http://www.htmleaf.com/jQuery/shijuecha/","http://www.htmleaf.com/jQuery/Menu-Navigation/","http://www.htmleaf.com/jQuery/Slideshow-Scroller/","http://www.htmleaf.com/jQuery/Image-Effects/","http://www.htmleaf.com/jQuery/Form/","http://www.htmleaf.com/jQuery/Tooltips/","http://www.htmleaf.com/jQuery/Table/","http://www.htmleaf.com/jQuery/Rating-Star-Rating/","http://www.htmleaf.com/jQuery/Tabs/","http://www.htmleaf.com/jQuery/Accordion/","http://www.htmleaf.com/jQuery/Lightbox-Dialog/","http://www.htmleaf.com/jQuery/Text-Link-Effects/","http://www.htmleaf.com/jQuery/Layout-Interface/","http://www.htmleaf.com/jQuery/Calendar-Date-Time-picker/","http://www.htmleaf.com/jQuery/Color-Picker/","http://www.htmleaf.com/jQuery/Chart/","http://www.htmleaf.com/jQuery/Buttons-Icons/","http://www.htmleaf.com/jQuery/jquery-tools/","http://www.htmleaf.com/html5/html5-canvas/","http://www.htmleaf.com/html5/SVG/","http://www.htmleaf.com/html5/html5donghua/","http://www.htmleaf.com/html5/html5youxi/","http://www.htmleaf.com/html5/html5muban/","http://www.htmleaf.com/html5/yinpinheshipin/","http://www.htmleaf.com/css3/animation/","http://www.htmleaf.com/css3/transform/","http://www.htmleaf.com/css3/transition/","http://www.htmleaf.com/css3/css3donghua/","http://www.htmleaf.com/css3/daohangcaidan/","http://www.htmleaf.com/css3/ui-design/"]


for x in src:
	
	try:
		print(x) #总分类
		jsonString=urllib.request.urlopen(x).read().decode("utf-8")
		pages=re.findall(pagePattern,jsonString) #分页
		list=re.findall(pattern,jsonString) #详情页地址

		maxpage=[]
		for p in pages:
			maxpage.append(p.split("_")[-1])
			# print(p)

		if len(maxpage)>1:
			
			maxpage.sort()
			totalPage=maxpage[-1]
			
			# print(totalPage)
			if int(totalPage) > 1:
				
				for m in range(2,int(totalPage)+1):
					nextpage=x+maxpage[0]+"_"+str(maxpage[1])+"_"+str(m)
					jsonString=urllib.request.urlopen(nextpage).read().decode("utf-8")
					#pagesnext=re.findall(pagePattern,jsonString)
					list2=re.findall(pattern,jsonString) #详情页地址
					list.extend(list2)




		
		
		for y in list:
			print(y)
			zipString=urllib.request.urlopen(y).read().decode("utf-8")
			# print(zipString)
			zipfile=re.findall(pattern2,zipString)
			# print(zipfile)
			for z in zipfile:
				urllib.request.urlretrieve(z,z.split("/")[-1])

				print(z)

			# if y==list[0]:
			# 	break

			# 	print(y)


		
		


	except Exception as e:
		print("异常")
		print(e)
		continue
	
	# if x==src[0]:
	# 	break

	
print("done-----")
				