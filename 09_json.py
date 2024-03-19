import json
import requests

# j1 = '{"ip":"192.168.0.130"}'
# print(j1) #{"ip":"192.168.0.130"}
# print(type(j1)) #<class 'str'>
#
# j2 = json.loads(j1)
# print(j2) #{'ip': '192.168.0.130'}
# print(type(j2)) #<class 'dict'>
# print(j2['ip']) #192.168.0.130

# data={
#     "no": 10,
#     "item": "재미있는 자바",
#     "price": 5000,
#     "qty":20
# }
# print(type(data)) #<class 'dict'>
#
# #dict를 문자열로만들어보자
#
# data2 = json.dumps(data)
# print(type(data2)) #<class 'str'>

#data가 문자열
data = '''
    {"dno": 10,
    "dname": "개발1팀",
    "dloc": "판교"}
'''

#연습) value부분만 모두출력
j1 = json.loads(data)

for key in j1:
    print(j1[key])

