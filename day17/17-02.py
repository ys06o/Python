import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
#[1] 크롤링 주소 확인:https://www.yes24.com/product/category/daybestseller?CategoryNumber=001

# url='https://www.yes24.com/product/category/daybestseller?CategoryNumber=001'

book_list=[]


#[2] 주소 분석 https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=1&pageSize=40&type=day&saleDts=&sex=M&age=20&goodsStatGb=06

for page in range(1,7):
    url='https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber={page}'


#[3] url 요청
    response=requests.get(url)

#[4] 요청한 url 성공 여부 확인
soup=BeautifulSoup(response.text,'html.parser')
# print(soup)


books=soup.select('#yesBestList>li') #여러개 가져오기
#[5] #책여러개 #yesBestList 여러개 책정보  li(책하나)
# 책하나당(.gd_name, .yes_b, .info_auth)
for book in books:
    gd_name=book.select_one('.gd_name').get_text().strip()
    yes_b=book.select_one('.yes_b').get_text().strip()
    info_auth=book.select_one('.info_auth').get_text().strip().split('\n')[0]
    
    book_list.append({'제목':gd_name,'가격':yes_b,'저자':info_auth})

#[6]리스트에 딕셔너리 포함하기
#[7]import time
time.sleep(2)

#[8]판다스에 넣어주기
print(book_list)

df=pd.DataFrame(book_list)
print(df)