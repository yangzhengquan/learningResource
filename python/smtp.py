#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = 'yangzhengquan000@126.com'  
receiver = '572157416@qq.com'  
# receiver = ['572157416@qq.com','yangzhengquan000@126.com']  #杨静

subject = '你好'  
smtpserver = 'smtp.126.com'  
username = 'yangzhengquan000@126.com'  
password = 'CHEN@wan'  
  
# msg = MIMEText('111','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg = MIMEText('<html><h1>当你看到这封邮件的时候，说明我已经成功使用了python的邮件功能。嘻嘻。</h1></html>','html','utf-8') 
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.126.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  