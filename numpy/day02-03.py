import numpy as np

#병합 .concatenate((x,y),axis=0) axis=0(행기준) 1(열기준)
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])

print(np.concatenate((x,y),axis=0)) #x아래로 y가 붙는다.
print(np.concatenate((x,y),axis=1)) #X오른쪽으로 y가 붙는다.

#정렬 #.sort()오름차순 정렬 .sort(n)[::-1] 내림차순 정렬
x=np.array([3,1,2,6,7,2])
print(np.sort(x))
print(np.sort(x)[::-1])  


#2차원 정렬
x=np.array([[12,1,2],[9,8,7]]) 
print(np.sort(x,axis=0)) #열기준 오름차순
print(np.sort(x,axis=1)) #행기준 오름차순
print(np.sort(x,axis=None)) #1차원 평탄화 후 정렬
print(np.sort(x,axis=None)[::-1]) #열기준 내림차순도 가능
#2차원 정렬 내림차순 주의할점: 2차원 슬라이싱 사용,[행슬라이싱,열 슬라이싱]
print(np.sort(x,axis=1)[:,::-1])

# np.sort() 복사본 반환 vs 배열.sort 차이점 원본을 건드는거기 때문에 
#복사본 vs새로운 배열을 생성하냐 그차이
x=np.array([5,1,3])
print(np.sort(x)) #[1 3 5]
y=x.sort()
print(y)


#.lensort()
#다중 정렬: 1차정렬 후 만약에 1차정렬에서 동일한 값이 존재하면 동일한 값끼리 2차정렬
x=np.array([25,30,22,24]) #1차원 배열 생성
y=np.array(['철수','영희','민수','영희']) #1차원리스트
z=np.lexsort((x,y))
print(y[z]) #y먼저 정렬후 ['민수' '영희' '영희' '철수']
print(x[z]) #동일한 값끼리 먼저 정렬 [22 24 30 25]


#필터링
x=np.array([10,20,30,40,50])
print(x>30)
print(x[x>30])

y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y%2==0)
print(y[y%2==0]) #1차원으로 결과 반환

#조건부 필러링, .where(조건,참,거짓)
print(np.where(x>30,x,-1)) #만약에 요소값이 30보다 크면 그대로 출력 아니면 -1을 출력
print(np.where(y%2==0,y,1))
#만약에 요소값이 짝수이면 요소값 그대로 출력, 아니면 1 출력
#자바의 삼항연산자랑 유사하다. #조건부 필러링이 가능

#마스크 필터링 ,조건식에서 False인 애들만 사용하겠다.
con1=x>30 #30초과을 마스크(가린다)
print(con1)
z=np.ma.array(x,mask=con1) #[10 20 30 -- --]
print(np.ma.sum(z))


#다수 조건 필터링
con2=y%2==0 #짝수조건 조건1
con3=y%4==0 #4의 배수 조건  조건2
print(y[con2&con3])
print(y[con2|con3]) #조건 하나만 충족하면
print(y[~con2]) #조건에 부정문 짝수->홀수로 출력된다.

#특정 조건을 충족하는 배열 반환,조건을 충족하는 요소만 추출가능
print(np.extract(y%2==0,y))