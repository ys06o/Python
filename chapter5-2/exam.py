#재귀 함수란? 현재 실행 중인 (자신의)함수를  다시 호출 하는것

#[1] 반복문으로 팩토리얼 구하기

def factorials(n):
    output=1
    
    for i in range(1,n+1):
        output*=i
    return output

print("5팩토리얼:",factorials(5))


#[2]재귀함수로 팩토리얼 구하기
def factorials(n):
    if n==0:
        return 1
    else:
        return n*factorials(n-1)

print(factorials(5))

#호출을 먼저 하고 return을 한번에 한다.



#[3]피보나치 수열 1
#1번쨰 수열:1,2번째 수열:2 ,N번째 수열:(N-1)+(N-2)
#func(4)->return  재귀(3)+재귀(2)
   #func(3)->return 재귀(2)+재귀(1)
    #func(2) return 재귀(1)+재귀(0)
        #func(1) return 1
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(50))

#문제점:재귀수가 많아서 계산식이 오래 걸린다.


#[4] 피보나치 수열2,메모화: 중간에 계산식을 저장하는 방식

dictionary={ #|결과를 저장하는 딕셔너리
    1:1,
    2:2
}


counter=0 #함수 밖 변수
def func4(n):
    global counter #함수 밖에 있는 변수를 호출
    counter+=1
    print("count:",counter)
    if n in dictionary: # 만약에 매개변수값이 딕셔너리에 존재하면?
      return dictionary[n]  #저장/메모 된 값을 리턴
    else:
        output=func4(n-1)+func4(n-2)
        dictionary[n]=output
        return output
print(func4(5 ))


최소=2
최대=10
전체사람수=6

memo={}

def 문제(남은사람수,최소사람수):   #10 #2
    key=str([남은사람수,최소사람수]) 
    if key in memo:
        return memo[key] 
    if 남은사람수<0:
        return 0
    if 남은사람수==0:
        return 1
    #경우의수  #6명이라고 가정 남은사람수
    count=0
    for i in range(최소사람수,최대+1):
        count+=문제(남은사람수-i, i)

    memo[key]=count
    print(memo)

    return count
        
    



print(문제(전체사람수,최소)) ##10명 최소 2명

help(print)