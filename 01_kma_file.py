import re
import requests
f = open("./Data/kma.csv","w", encoding="utf-8") #w:쓰기모드, r:읽기모드 -> 현재폴더에 Data폴더만들어
url = "https://devweather.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

text = requests.get(url).text #이사이트에있는 것을 긁어서 가져오는거야

# location = re.findall('<location wl_ver="3">(.+?)</location>',text,re.DOTALL)
# print(len(location)) #41
#
# # 모든 도시명을 추출해 출력
# citys = re.findall('<city>(.+?)</city>',text,re.DOTALL)
# print(citys)
# for city in citys:
#      print(city)
'''
<mode>A02</mode>
<tmEf>2024-02-26 00:00</tmEf>
<wf>맑음</wf>
<tmn>-2</tmn>
<tmx>9</tmx>
<reliability/>
<rnSt>10</rnSt>
'''
# location안에 도시명과 data안에 날짜, 날씨, 최고,최저를 가져오려면
locations = re.findall('<location wl_ver="3">(.+?)</location>',text,re.DOTALL)
for location in locations:
    city = re.findall('<city>(.+)</city>',location) #많지않으니까
    data = re.findall('<data>(.+?)</data>', location, re.DOTALL)
    for d in data:
        tmEf = re.findall('<tmEf>(.+?)</tmEf>', d)
        wf = re.findall('<wf>(.+?)</wf>',d)
        tmn = re.findall('<tmn>(.+?)</tmn>',d)
        tmx = re.findall('<tmx>(.+?)</tmx>',d)
        # print(city[0], tmEf,wf,tmn,tmx) #값이하나밖에없어도 리스트반환이라 0번째반환이라고적음

        f.write(city[0]+","+ tmEf[0]+","+wf[0]+","+tmn[0]+","+tmx[0]+"\n") #csv는 콤마로 구분하기때문에 이렇게 분리


    f.write("-"*50)
f.close();
print("날씨 정보를 수집하였습니다.")
#값가져온걸로 다양하게활용할수있어 db에 연결을하던가등등...
