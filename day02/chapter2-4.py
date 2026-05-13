#문자열의 format() 함수 , 자바에서
# System.out.printf("%s",10)와 유사한 기능을 하는 함수 비슷한개념이라고 보면됨
string_a="{}".format(10)
print(string_a,type(string_a)) #10

format_a="{} 만 원".format(5000) #중괄호 안에있는 값을 넣어줄 수 있다.
print(format_a) #5000 만 원
format_b="{} {} {}".format(1,"유재석",True)
print(format_b) #1 유재석 True
#주의할 점:{} 개수와 자료개수가 일치해야 한다. 일치하지 않으면 예외 발생
#format_c="{} {}".format(1,"유재석",True) #예외 발생

#특정 칸에 출력하기, {:자릿수d},{0:자릿수d}
output_a="{:5d}".format(52)
print(output_a) #52
output_b="{:05d}".format(52)
print(output_b) #00052

#기호를 붙여서 출력하기
output_c="{:+d}".format(52)
print(output_c) #+52
output_d="{:+d}".format(-52)
print(output_d) #-52


#부동소수점 출력하기
output_e="{:f}".format(3.141592)
print(output_e) #3.141592

#소수점 이하 자릿수 지정하기
output_f="{:+015f}".format(3.141592) #0으로 채우고, 부호 붙이고, 총 15자리로 맞추고, 소수점 이하 6자리까지 출력
print(output_f) #+0000003.141592

output_g="{:15.3f}".format(51.2737)
print(output_g) #잘린 소수점에서 반올림 된다. 51.274

#의미없는 소수점 제거하기 사용법:{:g}
output_g="{:g}".format(3.140000)
print(type(output_g)) #3.14



#대소문자 바꾸기
a="hello"
print(a.upper()) #HELLO
b="HELLO Python"
print(b.lower()) #hello python


#공백 제거하기 , strip()함수:문자열 양쪽에 있는 공백 제거, 
# lstrip():왼쪽 공백 제거
# rstrip():오른쪽 공백 제거

#사용처:크롤링한 데이터에서 공백 제거할 때
c="   hello   "
print(c.strip()) #hello 양쪽 공백 제거
print(c.lstrip()) #hello 왼쪽 공백 제거
print(c.rstrip()) #hello 오른쪽 공백 제거



#문자열 찾기
out_a="안녕안녕하세요".find("안녕") 
print(out_a) #0번인덱스에 "안녕"이 존재한다

out_b="안녕안녕하세요".rfind("안녕")
print(out_b)

print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")


#문자열 자르기 ,split("기준 문자")

out_c="10 20 30 40 50".split(" ")
print(out_c) #배열로 변환된다.



#f-문자열 vs .format() 선택
print(f'{10}')       
print("{}".format(10))
#결과는 동일하다.


a=input('a')
b=input('b')
sum=int(a)+int(b)
print("{}+{}={}".format(int(a),int(b),sum))



#1.
r=int(input('구의 반지름을 입력해주세요:'))
pi=3.141592
print("{}".format(4/3*pi*r**3))
print("{}".format(4*pi*r**2))



밑변=float(input('밑변:'))
높이=float(input('높이:'))

print("빗변의길이는:{}".format((밑변**2+높이**2)**0.5))

