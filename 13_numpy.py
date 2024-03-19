import numpy as np

def not_used():
    a = [1,2,3,4,5]
    b = np.array(a) #[1 2 3 4 5] ->파이썬 리스트를 갖고 넘파이배열만들기
    c = np.arange(10) #[0 1 2 3 4 5 6 7 8 9] ->순차적인 값을 갖는 넘파이배열 만들기

    #특정값으로 채워진 배열만들기
    a = np.zeros(10)
    print(a) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 실수

    b = np.zeros(10, dtype=np.int32)
    print(b) #[0 0 0 0 0 0 0 0 0 0] 정수

    c = np.ones(5)
    print(c) #[1. 1. 1. 1. 1.] 실수

    d = np.ones(5, dtype=np.int32)
    print(d) #[1 1 1 1 1] 정수

    e = np.zeros([3,4], dtype=np.int32)
    print(e) #3행 4열의 0으로 채워진 배열

    f = np.ones([2,1], dtype=np.int32)
    print(f) #2행 1열의 1로 채워진 배열

    g = np.full(10, 5) #5로 채워진거 10개 만들어줘
    print(g) #[5 5 5 5 5 5 5 5 5 5]

    h = np.full([3,4], 5)
    print(h) #3행 4열을 5로 채워진 배열

    a = np.arange(12)
    print(np.sum(a)) #66

    a = np.arange(12).reshape(-1,4) #4열
    print(np.sum(a)) #66

    #데이터분석에서는 '열'이 중요하게 여겨집니다
    print(np.sum(a, axis=0)) #열의 합 [12 15 18 21]
    print(np.sum(a, axis=1)) #행의 합 [ 6 22 38]

    #누적합: cumsum
    print(np.cumsum(a)) #[ 0  1  3  6 10 15 21 28 36 45 55 66]
    print(np.cumsum(a, axis=0)) #열별 누적합
    print(np.cumsum(a, axis=1)) #행별 누적합

    a = np.arange(12).reshape(-1,4)
    #이것과 동일하게 0으로 채워주세요
    b = np.zeros_like(a) #타입까지 동일하게됨
    c = np.zeros(a.shape, dtype=np.int32)
    print(b)
    print(c)

    d = np.full_like(a,100) #100으로 채워주세요
    print(d)

    print(np.random.random(3)) #0과 1사이에 난수 3개 만들어주세요
    print(np.random.random((2, 3))) #0과1사이의 난수 2행3열 만들어주세요
    #균등분포 :uniform
    print(np.random.uniform(size=(2,3)))
    #정규분포 : normal
    print(np.random.normal(size=(2, 3)))

    a = np.arange(10)
    b = np.random.choice(a,3) #a배열에서 3개를 뽑을거야
    print(b) #[8 9 0]

    a = [0,1,2,3,4,5,6,7,8,9,10,11]
    print(type(a)) #<class 'list'>

    b = np.array(a)
    print(type(b)) #<class 'numpy.ndarray'>

    print(a[0], a[-1], a[5:]) #0 11 [5, 6, 7, 8, 9, 10, 11]
    print(b[0], b[-1], b[5:]) #0 11 [ 5  6  7  8  9 10 11]

    print(a[0], a[-1], a[::-1]) #0 11 [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(b[0], b[-1], b[::-1]) #0 11 [11 10  9  8  7  6  5  4  3  2  1  0]

    #파이썬 리스트나 넘파이배열이나 기본적인 인덱싱이나 슬라이싱은 같아요!

    #2차원으로 만들어보자
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    b = np.array(a)
    print(a, type(a)) #[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] <class 'list'>
    print(b, type(b))
    #[[ 1  2  3  4]
     # [ 5  6  7  8]
     # [ 9 10 11 12]] <class 'numpy.ndarray'>

    print(a[0]) #[1, 2, 3, 4] 인덱싱 0번째 행
    print(b[0]) #[1 2 3 4]
    print(a[1:]) #[[5, 6, 7, 8], [9, 10, 11, 12]] 슬라이싱 0번째 행부터 끝까지
    print(b[1:])
    # [[ 5  6  7  8]
    #  [ 9 10 11 12]]

    print(a[0][0]) #1
    print(a[-1][-1]) #12
    print(b[0][0]) #1
    print(b[-1][-1]) #12

    a = np.arange(12).reshape(-1,4)
    #행도 거꾸로, 열도 거꾸로 -> fancy indexing
    b = a[::-1, ::-1]
    print(b)
    # [[11 10  9  8]
    #  [ 7  6  5  4]
    #  [ 3  2  1  0]]

    a = [80, 90, 65, 70, 92, 96]
    indices = [0, 1, 4, 5]
    result = [a[i] for i in indices]
    print(result) #[80, 90, 92, 96]

    a = np.array([80,90,65,70,92,96])
    print(a[[0,1,4,5]]) #[80 90 92 96] fancy indexing -> list만 가능

    arr80 = a[a>=80] #array로 바꿔야만 가능
    print(arr80) #[80 90 92 96]

    #다차원배열일때 fancy indexing
    a = np.arange(12).reshape(-1,4)
    print(a)
    # [[ 0  1  2  3]
    #  [ 4  5  6  7]
    #  [ 8  9 10 11]]
    row = [0,2] #1
    col = [1,2] #10

    b = a[row,col]
    print(b) #[ 1 10]

    a[0] = -1
    print(a)
    # [[-1 -1 -1 -1]
    #  [ 4  5  6  7]
    #  [ 8  9 10 11]]

    a[::]= -1
    print(a)
    # [[-1 -1 -1 -1]
    #  [-1 -1 -1 -1]
    #  [-1 -1 -1 -1]]

    a[:,0]=9
    print(a)
    # [[ 9 -1 -1 -1]
    #  [ 9 -1 -1 -1]
    #  [ 9 -1 -1 -1]]

#연습) 테두리가 1로 채워지고 속은 0으로 채워지는 5*5 배열을 만드세요
a = np.ones((5, 5))
a[1:-1, 1:-1] = 0
print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]

a = np.zeros((5,5))
a[0, :] = 1
a[-1, :] = 1
a[:, 0] = 1
a[:, -1] = 1
print(a)