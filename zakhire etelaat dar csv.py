
import mysql.connector
conn = mysql.connector.connect(user='root', password='1234',database='test', charset='utf8mb4',
collation='utf8mb4_general_ci')
cursor= conn.cursor()
cursor.execute("select * from mashins;")
chart=cursor.fetchall()

a=[]
b=[]
c=[]
d=[]
for row in chart:
    a.append(row[0])
    b.append(row[1])
    c.append(row[2])
    d.append(row[3])

cursor.close()
conn.close()

import pandas as pd # type: ignore

data = {
    'nam': a,
    'karkard': b,
    'az': c, 
    'gheimat': d
}

df = pd.DataFrame(data)

df.to_csv('car_data.csv', index=False)

print("etelaat dar file car_data.csv zakhire shod.")