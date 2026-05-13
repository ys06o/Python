#모듈 만들기 .py파일 만들기와 같다

#1. xxx.py파일을 생성한다. #
#2. 다른 .py파일 내에서 import하여 모듈을 불러온다.

import test_module as test


radius=test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))


#프로그램의 진입점:__name__=__main__
print(__name__)




#인터넷의 이미지 저장하기
from urllib import request

target=request.urlopen('https://www.hanbit.co.kr/images/common/logo_hanbit.png')
output=target.read()
print(output) #앞에 'b'가 붙는다. 바이너리 데이터로 반환이된다.

file=open('output.png','wb') #바이너리 파일 저장시 'wb'를 사용한댜.
file.write(output)  #파일쓰기
file.close() #파일닫기


