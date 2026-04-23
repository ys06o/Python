#함수 만들기

def 함수명():
  print("안녕하세요")
  print("안녕하세요")
  print("안녕하세요")

함수명()


#매개변수:함수 호출/사용시 인자값을 저장하는 변수

def func2(value,n):       #매개변수 2개 선언
  for i in range(n):      #매개변수 사용
    print(value)

func2("안녕하세요",10) #함수에게 인자값 2개를 전달


#가변길이 매개변수:매개변수의 개수가 변할 수 있다.

def func3(n,*values):       #매개변수의 *가변매개변수 사용시 [리스트] 타입으로 받는다.
  for i in range(n):
    for value in values:    #values=["안녕하세요","즐거운","파이썬 프로그래밍"]로 들어온다.
      print(value)

    print()

func3(3,"안녕하세요","즐거운","파이썬 프로그래밍")    


#기본 매개변수 :만약에 함수 사용/호출 시 인자값이 없으면 기본값을 대입해 줄 수 있다.

def func4(value,n=2):    #매개변수에 변수명=기본값 대입 
  for i in range(n):
    print(value)

func4("안녕하세요") #n=2가 기본값이므로 안녕하세요가  2번 출력



#키워드 매개변수:매개변수 이름을 직접 지정하여 매개변수에 대입하는 방법

def func5(*values,n=2):
  for i in range(n):
    for value in values:
      print(value)

func5("안녕","즐거운","파이썬 프로그래밍",3)  #n매개변수에 3 대입이 안된다.

func5("안녕","즐거운","파이썬 프로그래밍",n=6)  #직접 매개변수명을 작성하여 대입하면 된다.



#리턴이란? 함수 종료시 반환되는 키워드

#반환값 없는 리턴
def func6():
  return

print(func6())
#반환값 있는 리턴
def func7():
  return 100

print(func7())



def f(x):
  return x**2+2*x+1

print(f(3))


# 매개변수로 전달된 값을 모두 곱하는 함수
def mul(*values):
    result = 1
    for value in values:   #가변변수는 리스트 타입이다.
        result *= value
    return result
  
print(mul(2,3,4))

def func(valuea=10,valueb=20,*values):
  pass

print(func(1,2,3,4,5))


