import re
import requests
base = "https://www.hanbit.co.kr"
url = "https://www.hanbit.co.kr/store/books/new_book_list.html" #새책url 꼭 이렇게해야!
text = requests.get(url).text
# print(text)
text1 = re.findall('<!-- 책 리스트 -->(.+?)<!-- //책 리스트 -->', text, re.DOTALL)
print(text1[0])
arr = re.findall('<img src="(.+?)" alt="" class="thumb" />', text1[0])
#booktitle에있는 a를 찾아서 책제목으로 가져올거야
#<p class="book_tit"><a href="/store/books/look.php?p_code=B2814543303">만들면서 배우는 워드프레스&#40;전면 개정판&#41;</a></p>
arr2 = re.findall('<p class="book_tit"><a href=".+?">(.+?)</a></p>', text1[0]) #필요한게 책이름이니까 ()쳐야해
# print(len(arr2)) #20
arr = re.findall('<img src="(.+?)" alt="" class="thumb" />', text1[0])

for i in range(len(arr)):
    content = requests.get(base + ""+ arr[i]).content
    fname = arr2[i]+".jpg"
    fname = fname.replace("/","")
    f = open("./Hanbit2/"+fname,"wb")#파일이름
    f.write(content)
    f.close()
    print(fname+"을 다운받았습니다")