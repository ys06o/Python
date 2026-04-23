#튜플(): 소괄호를 이용하여 여러 자료들을 감싼 자료형,단 수정이 안된다.

tuple_test=(10,20,30)
#요소 호출 ,인덱스 사용
print(tuple_test)

#주의할점:수정이 안된다.
tuple_test[0]=1000 #TypeError: 'tuple' object does not support item assignment

#주의할점 요소가 1개인 경우
tuple_test2=(273,)
print(tuple_test2)

#튜플은 소괄호를 생략해도 된다.
tuple_test3=1,2,3,4,5
print(tuple_test3)
#할당 구문
[a,b]=[10,20]  #오른쪽에 있는 리스트에 자료들을 왼쪽 변수에 대입
print(a)
print(b)
(a,b)=(10,20)
print(a)
print(b)



#함수 리턴 값
def test():
    return 10,20

test()
