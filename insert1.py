import pymysql
import string
import random

db = pymysql.connect(host='localhost', port=3306,
                     user='root', passwd='ljy19980228', db='indexing', charset='utf8')

cursor = db.cursor()

sql = "INSERT INTO QueryPro30col(ID, Age, Name, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, \
    c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30) \
    VALUES (%s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s, %s,%s,%s)"
T = []

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(1, 1000001):
    age = random.randint(1,50)
    name = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c4 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c5 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c6 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c7 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c8 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c9 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c10 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c11 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c12 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c13 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c14 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c15 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c16 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c17 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c18 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c19 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c20 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c21 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c22 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c23 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c24 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c25 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c26 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c27 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c28 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c29 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    c30 = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 30)))
    T.append((i, age, name, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, \
        c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30))


try:
    cursor.executemany(sql, T)
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()
