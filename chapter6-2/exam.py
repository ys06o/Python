#예외 객체 : Exception 클래스
#예외가 발생할것 같은 곳에 코드 작성
#1.try~except 예외클래스명 as 변수명
#2.모든 예외 잡기: 마지막에
#3.강제 예외 발생
list_number=[52,273,32,72,100]
try:
    number_input_a=int(input('정수 입력>')) #int()에서 예외 발생 경우
    print(list_number[number_input_a])  #[] 에서 예외발생 경우
    raise NotImplementedError
    예외.발생()          #예상치 못한 예외는 Exception으로 처리하자
except ValueError as e:
    print('정수만 입력하세요')
except IndexError as e:
    print('인덱스를 벗어났습니다.')
except Exception as e:
    print(e)





