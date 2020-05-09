import pymysql

db = pymysql.connect(host='localhost', port=3306,
                     user='root', passwd='greeN7^Tr33', db='end2end', charset='utf8')

cursor = db.cursor()

sql = "INSERT INTO fixed1(ID, Age, Name) VALUES (%s,%s,%s)"
T = []

for i in range(1, 1000001):
    T.append((i, 20, 'Name'))


try:
    cursor.executemany(sql, T)
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()
