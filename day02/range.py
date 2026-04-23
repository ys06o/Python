#range 범위

#[1] 매개변수가 하나인 경우,0부터 n-1까지 리스트로 변환
print(list(range(5)))

#[2] 매개변수가 두개인 경우 s부터 n-1까지 리스트로 반환
print(list(range(0,5)))

#[3] 매개변수가 세개인 경우
print(list(range(0,10,2)))  #0부터 9까지 2씩 증가


#반복문과 범위의 활용

#for 반복변수 in range():
  #실행코드


#예시1
for i in range (1,11):
  print(i)


#예시2 1부터 10까지 홀수만 출력
for i in range(1,11,2):
    print(i)

#예시3 리스트와 범위 조합
array=[235,12,151,15415,123]

for i in range(len(array)): #0부터 리스트의 마지막 인덱스까지 순회
    print(array[i])


#vs


for element in array:
    print(element)





#예시4 역순으로 출력

for i in range(4,-1,-1): #4부터 0까지 1씩 감소
    print(i)


for i in reversed(range(5)): #reversed(리스트) ,리스트 역순으로 이터레이터 제공
    print(i)




# While 반복문
#무한루프
#while True:  #조건식
#    print(".",end="") #print(출력할 자료,end='')줄바꿈 처리를 안한다.



#1부터10까지 출력
i=1
while i<11:
    print(i)
    i+=1



#while 리스트 활용
list_a=[1,2,31,3,2,2,2]
while 2 in list_a: 
    list_a.remove(2)
    print(list_a)



import time

number=0

target_tick=time.time()+5
while time.time()<target_tick:
    number+=1




#break 
i=0
while True:
    print(i)
    i+=1
    input_text=input('종료할까요?>')
    if input_text in ['y','Y']:
        break
    


#continue 키워드
numbers=[5,15,6,20,7,25]

for number in numbers:
    if number<10: #반복변수가 10보다 작으면 다음반복변수로 이동 기존거는 건너뛰고
        continue
    print(number)



print(list(range(3,10,3)))