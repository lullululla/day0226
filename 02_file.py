#open("파일명","모드","인코딩")
#모드
#w:write r:read a:append(추가)

f = open("./Data/hello.txt","w", encoding="utf-8") #파일을 사용할때는 open이라는 함수사용
f.write("hello\n")
f.write("파이썬\n")
f.close()
print("파일을 만들었습니다.")