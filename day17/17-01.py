#웹 크롤링:웹페이지에서 존재하는 데이터들을 수집 하는 기술
#기초지식: HTML,CSS

#[1] html/css 식별자 찾기

#[2] 파이썬 크롤링
#안양시 날씨 ->현재 날씨
#1. 주소:https://search.naver.com/search.naver?query=안양날씨
#2.필요한 쿼리스트링 변수만 정리
#3.크롤링 선택자: .temperature_text

#[3] 정적 라이브러리

import requests #URL 요청 라이브러리
from bs4 import BeautifulSoup #요청된 URL HTML 조작 라이브러리

#(1) request.get(url) 가져올 url넣기
response=requests.get('https://search.daum.net/search?w=tot&q=안양날씨')
# print(response) #요청이 되는지 확인 <Response [200]>

#(2)요청된 url 에서 html 형식으로 파싱하기
# BeautifulSoup(response.txt,'html.paser')

soup=BeautifulSoup(response.text,'html.parser')
# print(soup) #html 형식으로 출력


#(3) 가져온 html 에서 특정한 요소(식별자) 가져오기 soup.select_one(식별자)
txt_temp=soup.select_one('.txt_temp') #온도 가져오기
print(txt_temp)

#(4) 가져온 요소에서 텍스만 추출, 마크업 텍스트 마크업 요소변수.get_text()
print(txt_temp.get_text())  #18.2도


