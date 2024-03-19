import requests

#한빛출판사-> f12-> 사진-> 전체src로가져오기
url = "https://www.hanbit.co.kr/data/books/B2814543303_l.jpg"
#글자는 text 이미지는 content
content = requests.get(url).content
f = open("./Data/새책.jpg", "wb") #글자가 아니니까 인코딩을 주지않고 바이너리파일이라고 설정 모드에-> wb
f.write(content)
f.close()
print("그림을 내려받았습니다.")