import numpy
#배열조작을 위하여 사용하는 libray

a = [10,20,30,40]
b = numpy.array(a)
print(a, type(a)) #[10, 20, 30, 40] <class 'list'>
print(b, type(b)) #[10 20 30 40] <class 'numpy.ndarray'>

c = b+1 #요소만큼 동작하는거야
print(c, type(c)) #[11 21 31 41] <class 'numpy.ndarray'>

# d = a+1
# print(d) #numpy에서만 동작하기때문에 에러발생
 