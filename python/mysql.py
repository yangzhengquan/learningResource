import pymysql
conn = pymysql.connect(user='root', passwd='root',
                 host='localhost', db='mysql')
cur = conn.cursor()
cur.execute("SELECT * FROM user")
for r in cur:      
      print("row_number:"+str(cur.rownumber))        
      print("host:"+str(r[0])+"user:"+str(r[1])+"age:"+str(r[2])) 
cur.close()    
conn.close() 