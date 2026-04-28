#[1] numpy란? 고성능 수치 계산 라이브러리
#[2] 설치 터미널에서 pip install numpy
#[3]numpy 불러오기
#[4]numpy 버전 확인하기
import numpy 
print(numpy.__version__) #2.4.4 버전

#[1] 넘파이 배열 생성 

x=[1,2,3,4] #일반 리스트
print(x) #[1, 2, 3, 4]
x=numpy.array([1,2,3,4,5]) #.array([1차원 리스트]) #넘파이에 1차원 배열
print(x) #[1 2 3 4 5] 차이가 있음 출력에

x=numpy.array([[1,2,3],[4,5,6]])  #2차원 배열 .array[[1차원리스트],[1차원리스트]] 리스트안에 또 리스트를 삽입
print(x)

x=numpy.zeros((2,3)) #.zeros((행,열)) 행과 열 만큼의 0으로 초기화 
print(x)

x=numpy.ones((2,3))  #.ones((행,열)) 행과 열 만큼의 1로 초기화 
print(x)

x=numpy.full((2,3),10)   #.full((행,열),원하는 숫자) 행과 열 만큼의 원하는 숫자 값으로 초기화
print(x)

#.arrang(시작값,끝값,단위) 시작부터 끝까지 단위만큼 증가
x=numpy.arange(0,10,2) #파이썬에 range랑 비슷한 개념
print(x)

# .lingspace(시작,단위,총개수)
x=numpy.linspace(0,10,5)  #0부터 10까지 5개로 쪼갠다  
print(x)





#넘파이 호출
import numpy as np

#[2] 배열의 주요 속성
# .shape 현재 배열의 크기를 튜플로 반환
x=np.array([[1,2,3],[4,5,6]])
print(x.shape) #(2,3)

# .dtype 현재 배열내 데이터 타입을 반환 하나라도 float타입이면 float64로 반환함
x=np.array([1.0,2.0,3.0])
print(x.dtype)

# .size , 현재 배열내 모든 요소 수
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x.size)

# .ndim 차원수 반환 현재 몇차원인지
x=np.array([1,2,3])
print(x.ndim)  



#[3] 배열의 타입 .array(자료,dtype=numpy.타입명)
#8bit란 이진수가 8개 1byte ->kb->mb->gb->
#즉 bit가 많을수록 더 많은 자료를 저장할 수 있다.
x=np.array([1,2,3],dtype=np.int32)
print(x.dtype) #정수형 32bit bit가 클수록 더 많은 정보를 제공한다.
x=np.array([1.0,2.0,3.0],dtype=np.float64)
print(x.dtype) #오차를 줄이기 위해서는 큰 비트를 쓰는게 좋다 #오차 최소화

x=np.array([True,False,True])
print(x.dtype) #bool 논리형

x=np.array(['a23','b','c2'],dtype=np.bytes_) #
print(x.dtype) #문자열을 바이트형태로 저장한다.

# .astype(numpy.변환할 타입명)
x=np.array([1.5,2.3,4.5]).astype(np.bool)
print(x.dtype)
print(x)
y=x.astype(np.int32)
print(y) #소수점이 짤려서 출력된다. 정수는 소수점을 표현할 수 없기 때문에 정수형태로 출력
