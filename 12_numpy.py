import numpy as np #애칭사용

def notused():
    # a=[10,20,30,40,50]
    #
    # b = np.array(a);
    # print(b,type(b)) #[10 20 30 40 50] <class 'numpy.ndarray'>

    a = np.arange(5) #5개배열만들어주는거야
    print(a, type(a)) #[0 1 2 3 4] <class 'numpy.ndarray'>

    a = np.arange(10)
    b = np.arange(1,11,1)
    print(a) #[0 1 2 3 4 5 6 7 8 9]
    print(b) #[ 1  2  3  4  5  6  7  8  9 10]

    c = np.arange(1,20,2)
    print(c) #[ 1  3  5  7  9 11 13 15 17 19]

    d = np.arange(10,-1,-1)
    print(d) #[10  9  8  7  6  5  4  3  2  1  0]

    a = [1,2,3,4]
    b = [1.0,2.0,3.0,4.0]
    c = ['사과','포도','수박','오렌지']
    d = [True, True, False, True]

    data_a = np.array(a)
    data_b = np.array(b)
    data_c = np.array(c)
    data_d = np.array(d)

    print(data_a.shape, data_a.ndim, data_a.dtype) #몇행몇열의 배열인지 알려주는거, 차수알려주는거,데이터요소의 타입
    #(4,) 1 int32-> (4행1열), 1개, int형이다
    print(data_b.shape, data_b.ndim, data_b.dtype) #(4,) 1 float64
    print(data_c.shape, data_c.ndim, data_c.dtype) #(4,) 1 <U3
    print(data_d.shape, data_d.ndim, data_d.dtype) #(4,) 1 bool

    arr = [[1,2,3],[4,5,6]]
    data = np.array(arr)
    print(data.shape, data.ndim) #(2, 3) 2

    #차수를 바꿔보자
    a = [1,2,3,4,5,6,7,8,9,10]
    b = np.array(a)
    # c = b.reshape(2,-1) #알아서해
    c = b.reshape(-1,5) #알아서해
    print(c)
    #'''
    # [[ 1  2  3  4  5]
    #  [ 6  7  8  9 10]]
    # '''
    print(c.shape, c.ndim) #(2, 5) 2


    a = range(5)
    b = np.arange(5)
    c = np.array(a)
    print(a, type(a)) #range(0, 5) <class 'range'> ->반복문을사용할때 range사용
    print(b, type(b)) #[0 1 2 3 4] <class 'numpy.ndarray'>
    print(c, type(c)) #[0 1 2 3 4] <class 'numpy.ndarray'>

    #연습) 0에서 5까지 정수가 들어있는 2행 3열의 배열을 만들어봅니다(세가지방법)
    a = np.array([[0,1,2],[3,4,5]])
    print(a)

    b = np.array(range(6)).reshape(2,-1)
    print(b)

    c = np.array(range(6)).reshape(-1,3)
    print(c)

    '''
    [[0 1 2]
     [3 4 5]]
    '''

    # 연습) 다음의 a를 1차원리스트로 만들어봅니다
    a = np.arange(6).reshape(2,3)
    print(a)

    b = a.flatten() #[0 1 2 3 4 5]
    print(b)

    c = a.reshape(6)
    print(c) #[0 1 2 3 4 5]

    d = list(a.reshape(6))
    print(d, type(d)) #[0, 1, 2, 3, 4, 5] <class 'list'>

    d = list(a.reshape(a.size))
    print(d)  #[0, 1, 2, 3, 4, 5]

    e = list(a.reshape(-1))
    print(e) #[0, 1, 2, 3, 4, 5]

    a = np.arange(3)
    print(a) #[0 1 2]
    a = a+1
    print(a) #[1 2 3] *****
    print(a+1) #[2 3 4]
    #broadCasting   배열의 원소만큼 연산을 수행
    print(a**2) #a의제곱 #[1 4 9]
    print(a>1) #[False  True  True]
    print(a[a>1]) #Bool 인덱싱 ->True인것만 추출해라

    a = [0,1,2,3,4,5,6,7,8,9]
    #인덱싱: 특정위치에 있는것을 가져오는것
    print(a[0], a[1]) #0 1
    print(a[-1], a[-2]) #9 8 #맨끝: -1

    #슬라이싱: 범위에있는것을 가져오는것
    print(a[3:7]) #start 3 end 7(6까지) #[3, 4, 5, 6]
    print(a[:7]) #start를 생략, 처음부터- #[0, 1, 2, 3, 4, 5, 6]
    print(a[5:]) #end를 생략, #[5, 6, 7, 8, 9]
    print(a[:]) #전부다 #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a[::2]) #[0, 2, 4, 6, 8]
    print(a[1::2]) #[1, 3, 5, 7, 9]
    print(a[::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # print(a[9:-1:-1]) -> 끝과끝이라서 []출력

    a = np.arange(3)
    b = np.arange(3)
    print(a,b) #[0 1 2] [0 1 2]
    print(a+1) #[1 2 3] BroadCasting
    print(a+b) #[0 2 4] 각 배열의 원소끼리 연산 Vector Operation
    print(a**b) #[1 1 4]
    print(a>b) #[False False False]

#연습) 5개의 변수에 대하여 각각 덧셈을 실행해봅니다.
a = np.arange(3)
b = np.arange(6)
c = np.arange(3).reshape(-1,3)
d = np.arange(6).reshape(-1,3)
e = np.arange(3).reshape(3,-1)

print(c) #[[0 1 2]]
print(d) #[[0 1 2]
        # [3 4 5]]
print(e) #[[0]
         #[1]
         #[2]]
print("-"*6)
print(a+c) #[[0 2 4]] BroadCasting(차수가다른게)// 차수가같으면 Vector Operation
print(a+d)
print(a+e)
print("-"*6)
print(b+e)
print("-"*6)
print(c+d)
print(c+e)