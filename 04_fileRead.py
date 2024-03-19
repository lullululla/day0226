f = open("./Data/hello.txt","r", encoding="utf-8")
lines = f.readlines() #리스트타입-> 파일의 내용을 모두 읽기 lines
for row in lines:
    print(row, end=" ")
f.close()
print("파일의 내용을 모두 읽어들였습니다.")