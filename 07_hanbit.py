import re
import requests
base = "https://www.hanbit.co.kr"
url = "https://www.hanbit.co.kr/store/books/new_book_list.html" #새책url 꼭 이렇게해야!
text = requests.get(url).text
# print(text)
text1 = re.findall('<!-- 책 리스트 -->(.+?)<!-- //책 리스트 -->', text, re.DOTALL)
print(text1) #['\r\n    <div class="sub_book_list_area">\r\n            \r\n        <li class="sub_book_list">\r\n ...
arr = re.findall('<img src="(.+?)" alt="" class="thumb" />', text1[0])
i=1 #1씩증가해서 파일이름넣을거야
for row in arr:
    print(row)
    content = requests.get(base+""+row).content
    f = open("./Hanbit/"+str(i)+",jpg","wb")
    f.write(content)
    f.close()
    print('book_'+str(i)+'를 저장')
    i+=1
print('모두 저장')

