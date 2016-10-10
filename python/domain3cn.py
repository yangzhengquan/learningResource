#!/usr/bin/python
#coding:utf-8
import urllib.request
import json
list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list1=["a", "b"]

i=0

token="check-web-hichina-com%3Ah1ddwmc3g67dik8si4rzbc1obsrrlaep"
tokens=["check-web-hichina-com%3Awmmsxdne3e816bzzvi0jksdal8hwjs8q","check-web-hichina-com%3A9r2v7u0o0htrstjv9j7mmaa0ouelgnfl","check-web-hichina-com%3Akld1i9nixeevb0r1ru43h50v10e48xdc","check-web-hichina-com%3Aqycxib18zq2tm0ifwkj2xvodzpn8blzk"]
ec=0

for a in list:
	
		
	for b in list:
		for c in list:
			
				
				# print(a+b+c+d)
				jsonString=urllib.request.urlopen("http://pandavip.www.net.cn/check/checkdomain?token="+token+"&domain="+a+b+c+".cn").read().decode("utf-8")
				print(a+b+c)
				try:
					dic1=json.loads(jsonString[1:-2])
					if dic1["success"] == "true" and dic1["module"][0]["avail"] == 1:
						# pass
						fo=open("demain3cn.txt","a+")
						fo.write(dic1["module"][0]["name"]+"\n")
						#fo.write("\n")
						fo.close()
						print("============"+a+b+c)

				except Exception:
					ec+=1
					token=token[ec]
					
					print(jsonString)
					continue

				else:
					pass
				finally:
					pass


				

				# if i%10 == 9:
				# 	fo.close()
				# i+=1



print("done:---------------------------------")