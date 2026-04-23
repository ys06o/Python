
#변수:하나의 자료 저장하는 메모리 공간


pi=3.14151515 
print(pi) #변수 참조 ,변수가 갖는 자료 반환
print(pi+pi)

#주의할 점

print(pi,"입니다.") #연결

#타입의 유연성 =동적 타입, 단점:타입 식별 어렵다.

# 자바 또는 c언어 int pi=3


#복합 대입 연산자

number=100
number+=10
print(number) #110
number-=20
print(number) #90
number*=10
print(number) #900
number/=10
print(number) #90.0


#사용자 입력  input()함수:사용자 입력 받는 함수 주의할 점:콘솔에 입력하는 구조로 무조건 문자열로 반환된다.
string=input("인사말을 입력하세요")
print(string)

print(type(string)) #str


#문자열을 숫자로 변환하는 함수 int(), 사용처:http 요청에서 숫자 데이터 받을 때, 사용자 입력 받을 때
#타입 변환 해야하는 이유:자료를 사용할 때 서로다른 타입간의 예외가 발생할 수 있기 때문에 ex)int+str -> 예외 발생, int+int -> 정상 작동
string_a=input("입력a>")
int_a=int(string_a)
print(type(int_a)) #int

string_b=int(input("입력b>"))
print(type(string_b)) #int 

#동일한 결과


string_c=float(input("입력c>"))
print(type(string_c)) #float


#숫자를 문자열로 바꾸기
pi=3.141592
pi_string=str(pi)
print((type(pi_string))) #str



#1.타입:string,number,boolean
#2.문자열 표현"",' ',""" """
#3.이스케이프문자:\n(줄바꿈),\t(탭),\\(역슬래시),\'(작은따옴표),\"(큰따옴표)  
#4.문자열길이:len()함수
#5.문자열 인덱싱:문자열[인덱스]
#6.문자열 슬라이싱:문자열[시작인덱스:끝인덱스]
#7.숫자 종류:int,float
#8.사칙연산자:+,-,*,/ // %
#9.복합 대입 연산자:+=,-=,*=,/=
#10.출력:print()함수
#11.입력:input()함수
#12.타입 변환: int(),float(),str()



#1.타입:string,number,boolean
#2.문자열 표현:' ' " " """ """
#3.이스케이프문자:\n,\t \\ \' 등등
#4.문자열길이:len()
#5.문자열 인덱싱:문자열[인덱스]
#6.문자열 슬라이싱:문자열[시작인덱스,끝인덱스]
#7.숫자 종류:int,float
#8.사칙연산자:+ - * / // % **
#9.복합 대입 연산자:+=, =-, =/, *=
#10.출력:print
#11.입력:input
#12.타입 변환: int(), float(),str()



#타입:string,number,boolean
#문자열 표현
# // ** %
#문자열 길이:len()
#문자열 인덱싱:문자열[인덱스]
#문자열 슬라이싱:문자열[시작인덱스,끝인덱스]
