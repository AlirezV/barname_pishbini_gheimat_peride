import requests
from bs4 import BeautifulSoup

r = requests.get("https://divar.ir/s/tehran/car?q=%D9%BE%D8%B1%D8%A7%DB%8C%D8%AF")
soup = BeautifulSoup(r.text, 'html.parser')

ads = soup.find_all("div", class_="kt-post-card__info")

for ad in ads:
    
    divs = ad.find_all("div", class_="kt-post-card__description")                     
    nam=ad.find("h2", class_="kt-post-card__title")
    karkard = divs[0]
    gheimat = divs[1]
    az=ad.find("span", class_="kt-post-card__bottom-description kt-text-truncate")
    
    a=nam.text
    b=karkard.text
    c=gheimat.text
    d=az.text
    #print("ماشینه: %s با کارکرده: %s با قیمته: %s از: %s موجود می باشد!" %(a,b,c,d))
    import mysql.connector
    conn = mysql.connector.connect(user='root', password='1234',database='test', charset='utf8mb4',
    collation='utf8mb4_general_ci')
    cursor= conn.cursor()
    cursor.execute("insert into mashins values (\"%s\",\"%s\",\"%s\",\"%s\");" % (a,b,d,c))
    conn.commit()
    print("maghadir vared database shod!")
    conn.close()




