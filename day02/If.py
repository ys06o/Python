#파이썬 조건문/분기문 ,  if 조건:

number=int(input('정수 입력: '))
if number>0:
    print('양수입니다.')  #java와 다르게 들여쓰기를 이용하여 실행문을 구분한다.


if number<0:
    print('음수입니다.')

if number==0:
    print('0입니다.')





#if~else
number1=int(input('정수 입력: '))
if number1%2==0:
    print('짝수입니다.')
else:
    print('홀수입니다.')



if number1%2==0:
    print('짝수입니다.')
elif number1%2==1:
    print('홀수입니다.')
else:
    print('0입니다.')



#조건이 3개 이상 일 때:[1] if if if vs if~elif