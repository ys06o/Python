#리스트란? 여러 자료들을 모아 하나의 자료로 구성하는 자료형
#리스트는 대괄호로 감싸고, 요소는 쉼표로 구분한다.
#인덱스란? 자료가 저장된 순서,0부터 시작한다.

list_a=[273,32,"문자열",True]
print(list_a[0]) #273
print(list_a[1:3]) #[32, '문자열'] #슬라이싱도 가능

list_a[1]='변경값' #리스트의 요소는 변경 가능하다.
print(list_a) #[273, '변경값', '문자열', True]

print(list_a[-1]) #True
print(list_a[-2]) #'문자열'

print(list_a[2][1]) #문자열의 1번째 인덱스, '자' 출력

list_a[1]=['변경값1','변경값2'] #리스트 안에 리스트도 가능
print(list_a) #[273, ['변경값1', '변경값2'], '문자열', True]



#리스트의 연산

list_a=[1,2,3]
list_b=[4,5,6]

#[1]연결
print('#리스트의 덧셈')
print(list_a+list_b) #[1, 2, 3, 4, 5, 6]

#[2] *반복
print('리스트의 반복')
print(list_a*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 길이 구하기
print('리스트의 길이')
print(len(list_a)) #3
print(len(list_b)) #3


#리스트의 요소 추가하기
list_a.append(4) #append()는 리스트의 맨 뒤에 요소를 추가하는 함수
print(list_a) #[1, 2, 3, 4]

#리스트의 중간에 요소 추가하기
list_a.insert(1,10) #insert()는 리스트의 원하는 위치에 요소를 추가하는 함수, 첫 번째 인자는 위치, 두 번째 인자는 추가할 요소
print(list_a) #[1, 10, 2, 3, 4]


#리스트에 요소 제거하기

list_a=[0,1,2,3,4,5]
#[6] del 리스트명[인덱스]
del list_a[1]
print(list_a) #[0,2,3,4,5]

#[7] 리스트명.pop(인덱스)
list_a.pop(2)
print(list_a) #[0,2,4,5]
list_a.pop()
print(list_a) #[0,2,4] pop()안에 매개변수를 입력하지 않으면 마지막 요소가 제거된다.

# 슬라이싱이란? 인덱스로 구성된 자료들(문자열/리스트)을 요소를 선택할 수 있는 기능
#[시작인덱스:끝인덱스:단계] 증감이랑 비슷한 개념
print(list_a[::-1]) #[4,2,0] 역순으로 출력된다.


print(list_a) #[0,2,4]
print(list_a[0::2])#[0,4]  #0부터 마지막 인덱스까지 2칸씩 이동

#[8]리스트명.remove(제거할 자료)
list_a.remove(0) #해당리스트에서 자료가 존재하면 삭제 0이삭제 된다.
print(list_a)

#[9]clear 리스트의 모든 요소 삭제
list_a.clear()
print(list_a)


#sort정렬
list_a=[123,14,15,123]
list_a.sort() 
print(list_a) #오름차순이 기본 [14, 15, 123, 123]

#내림차순
list_a.sort(reverse=True)
print(list_a)

#[11] in연산자 내부에 있는지 확인 True or False로 출력
print(103 in list_a)
print(123 in list_a)

print(2222 not in list_a) #부정문도 사용가능

