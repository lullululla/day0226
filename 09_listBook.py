import requests
import json

f = open("./Data/listBook.csv", "w", encoding="utf-8")
url = "http://192.168.0.130:52273/listBook"
text = requests.get(url).text

j1 = json.loads(text)
for book in j1:
    f.write(str(book['BOOKID']) + "," + book['BOOKNAME'] + "," + book['PUBLISHER'] + "," + str(book['PRICE']) + "\n")
print("다운로드가 완료되었습니다.")

f.close()
