#파일처리
#open(파일경로,읽기모드) ,file 객체가 반환이 된다.
#읽기모드 w:새로쓰기 ,a:이어쓰기, r:읽기모드
#(1) open 함수를 이용하여 지정된 경로의 파일 쓰기
file=open('./chapter5-3/basic.txt','w') #현재.py 파일에 basic.txt 가 생성된다.
#(2) .write(쓸 내용)
file.write('hello')

#(3).close 함수를 이용한 안전하게 스트림 닫기
file.close()

#(4) with 키워드를 이용한 .close()자동 닫기
with open('./chapter5-3/basic2.txt','w',encoding='utf-8') as file:
    file.write("basic2 테스트")

#스트림이란, 데이터가 흐르는 길 ,바이트단위,프로그래밍언어가 외부 자료와 연결할때 (파일,jdbc,네트워크)

#(5) .read() 함수를 이용한 파일 읽어오기
with open('./chapter5-3/basic.txt','r') as file:
    contents=file.read()

print(contents)     #hello가 출력되는걸 알수있음


import random

hanguls=list('가나다라마바사아자차카타파하')

with open("./chapter5-3/info.txt",'w',encoding="utf-8") as file:
    for i in range(1000):
        name=random.choice(hanguls)+random.choice(hanguls)
        weight=random.randrange(40,100)
        height=random.randrange(140,200)

        file.write(f"{name},{weight},{height}\n")



with open("./chapter5-3/info.txt", 'r',encoding="utf-8") as file:
    for line in file:
        # 1. 공백 제거 및 분할
        data = line.strip().split(", ")
        
        # 데이터가 3개가 아니면 건너뛰기 (예외 처리)
        if len(data) != 3:
            continue
            
        (name, weight, height) = data
        
        # 2. BMI 계산 (수식은 그대로 유지)
        # BMI = weight / (height/100)^2
        bmi = int(weight) / ((int(height) / 100) ** 2)
        
        # 3. 결과 판정
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        # 4. 출력 (리스트 내부 콤마 확인 및 포맷팅)
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {:.2f}", # 소수점 2자리까지 출력하면 깔끔합니다
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print() # 줄바꿈용



numbers=[1,2,3,4,5,6]
print("::".join(map(str,numbers)))

numbers=list(range(1,10+1))

print("#홀수")
print(list(filter(lambda x:x%2==1,numbers)))
print()
print(list(filter(lambda x:x>=3 and x<7,numbers)))
print()

print(list(filter(lambda x:(x*x)<50,numbers)))

