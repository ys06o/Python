import numpy as np

#배열 연산 ,두 배열간의 동일한 위치끼리 연산을 수행
x=np.array([1,2,3])
y=np.array([4,5,6])

print(x+y)   #[5 7 9]
print(x-y)   #[-3,-3,-3]
print(x*y)   #[4,10,18]
print(x/y)
print(x%y)   #[1 2 3]
print(x**4)
print(y//x)

print(x>y)
print(x<y)
print(x+10)
print(y*2)


#논리 연산     
x=np.array([True,False,True])
y=np.array([False,False,True])
print(np.logical_and(x,y))   #and 둘다참이면 참
print(np.logical_or(x,y))    #or 하나라도 참이면 참
print(np.logical_not(x,y))


#루트(수학에서쓰는)
y=np.array([1,4,9])
print(np.sqrt(y).astype(int))



#2차원 배열 비교
y=np.array([[1,2,3],[4,20,6]])
print(y>3)
x=np.array([1,10,3]) #1차원 행1개  y 2차원은 행이 n개


# .all()
x=np.array([True,False,True])
print(np.all(x))  #모두 참이면 참 all  and연산자랑 유사
print(np.any(x))  #하나라도 참이면 참  or연산자랑 유사

# .equal(x,y): 두배열의 요소들이 모두 같으면 참
x=np.array([1,2,3])
y=np.array([1,2,3])
z=np.array([1,2,3])
print(np.array_equal(x,y))