#표준 모듈:파이썬 내장 라이브러리
#외부 모듈:설치형 라이브러리
#호출방법: import 모듈명

#from 모듈명 import 가져오고싶은함수또는 변수
#from 모듈명 import * :모두 가져오기
#식별자 부여:  import 모듈명 as 식별자명
import math #import 모듈명

print(math.sin(1)) #호출한 모듈에서 sin 함수 호출, .접근연산자
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5)) #내림
print(math.ceil(2.5)) #올림

print(math.exp2())

from math import sin,cos,tan,floor,ceil

print(sin(1))
import math as m
print(m.sin(1))



#ramdom module
import random
print(random.random()) #0.0~1.0사이의 난수 생성

print(random.uniform(10,20))  #uniform(시작값,끝값) 지정된 범위사이의 난수를 생성
print(random.randrange(10,1000000000000)) #int형식으로 (시작값,끝값)범위에 난수 생성

print(random.choice([10,24,5,2,5])) #choice([리스트]) #리스트내 랜덤 요소를 반환

a=[1,2,3,51,5]

print(random.shuffle(a))

print(random.sample([1,2,3,4,5],k=2)) #리스트의 요소중 k개를 뽑는다.


#OS 모듈
import os
print("현재 운영체제:",os.name) #nt:윈도우의 커널
print("현재 폴더:",os.getcwd()) #현재 폴더: C:\Users\sku-102-04\Desktop\python
print("현재 폴더의 내부의 요소:",os.listdir())
#['.git', 'basic.txt', 'chapter4-4', 'chapter5-1', 'chapter5-2', 'chapter5-3', 'chapter6-2', 'chapter7', 'day01', 'day02', 'practice']
os.mkdir("hello") #hello라는 폴더가 생성된다.
os.rmdir("hello") #hello라는 폴더가 삭제된다. #remove diractory


with open ('original.txt','w') as file:
    file.write('hello')
os.rename('original.txt','new.txt') #파일명 변경 가능

os.remove('new.txt') #파일 삭제

os.system('dir')
    


#datetime  모듈
import datetime
now=datetime.datetime.now()
print(datetime.datetime.now()) #2026-04-24 09:55:15.216316
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#형식:  y연도  m 월 d일 H시 M분 S초
output_a=now.strftime('%Y-%m-%d %H:%S')
print(output_a)



#시간 계산
output=now.replace(year=(now.year+1),month=(now.month-1),minute=(now.minute-1))
print(output)


#time 모듈
import time
print('5초간 일시정지') #스레드란 코드가 실행되는 흐름의 단위
time.sleep(5)
print('종료')


#urllib 모듈 #큰의미는 없다. #가벼운 정적인 페이지면 쓰면 좋다.

from urllib import request #from이용한 특정한 함수만 가져오기
target=request.urlopen('https://google.com')
output=target.read()
print(output)

#opearator itemgetter() 함수 알아둘것

import os

def read_folder(path):
    #폴더의 요소 읽어 들이기
    output=os.listdir(path)
    #폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            read_folder(path+'/'+item)
        else:
          print("파일:",item)
      
read_folder(".")        