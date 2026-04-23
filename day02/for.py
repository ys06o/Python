#리스트와 반복문
# for 반복변수 in 반복할수있는자료:
    #코드작성


array=[23,24,16,63,211]

for e in array:
    print(e)


for 요소 in "안녕하세요":
    print(요소)



#중첩 리스트 #중첩 반복문 #2차원 리스트

list_of_list=[
    [1,2,3], #1행 3열
    [4,5,6,7], #2행 4열
    [8,9]     #3행 2열
]

for row in list_of_list:
    print(row) #각 행 출력
    for col in row:
      print(col) #각 행의 열 출력


list_a=[1,2,3]
print(list_a) #리스트 그자체
print(*list_a) #리스트 그자체가 아닌 전개
#리스트는 첫번째 인덱스를 참조한다.



list_a=[0,1,2,3,4,5,6,7]
list_a.extend(list_a)
print(list_a)

numbers=[273,103,4]

for n in numbers:
    if n%2==0:
        print(f"{n}는 짝수입니다.")
    else:
        print(f"{n}는 홀수입니다")

for n in numbers:
    n2=len(str(n))
    print(f"{n}은 {n2}자릿수입니다.")


numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for number in numbers:
    output[number%3-1].append(number)
#3구역 나누기 위해서, -1이유는 인덱스 0부터 표현하기위해서
print(output)



