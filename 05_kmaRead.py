#kma,csv 파일을 읽어들여 출력
f = open("./Data/kma.csv","r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line, end=" ")
f.close()



