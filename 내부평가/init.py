import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
import koreanfont                   # 한글폰트


#book_list = []

#for page in range(1, 25):
    #url = f"https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber={page}&pageSize=40"
    #response = requests.get(url)

    #soup = BeautifulSoup(response.text, 'html.parser')
    #books = soup.select('#yesBestList>li')

    #for book in books:
        #gd_name = book.select_one('.gd_name').get_text().strip()
        #yes_b = book.select_one('.yes_b').get_text().strip()
        #sale_data = book.select_one('.info_row.info_rating span.saleNum').get_text().strip().split()
        #saleNum = sale_data[1] if len(sale_data) > 1 else sale_data[0]
        #year = book.select_one('.info_row.info_pubGrp .authPub.info_date').get_text().strip()
        #book_list.append({'도서 제목': gd_name, '가격': yes_b, '판매지수': saleNum, '출판년월': year})

    #print(f"{page}페이지 크롤링 완료 (현재 {len(book_list)}개 저장됨)")
    #time.sleep(1)

#df = pd.DataFrame(book_list)
#df.to_csv('내부평가/books.csv', index=False, encoding='utf-8-sig')



books_df = pd.read_csv('내부평가/books.csv', encoding='utf-8-sig')

# 1. 가격: 쉼표·"원" 제거 후 int 변환
books_df['가격'] = books_df['가격'].str.replace(',', '').str.replace('원', '').astype(int)

# 2. 출판년월 데이터 전처리
#가. 연도 컬럼 추출
books_df['연도'] = books_df['출판년월'].str.split('년').str[0].astype(int)

#나. 월 컬럼 추출,
books_df['월'] = books_df['출판년월'].str.split('년').str[1].str.replace('월', '').astype(int)

print(books_df.info())
print(books_df.head())


#평균 가격 계산
print("평균 가격:", int(books_df['가격'].mean()),"원")
#최고 가격 계산
print("최고 가격:", books_df['가격'].max(),"원")
#최저 가격 계산
print("최저 가격:", books_df['가격'].min(),"원")

#출판 연도 분석
#연도별 도서 수 계산
books_by_year = books_df['연도'].value_counts().sort_index()
print("연도별 도서 수:")
print(books_by_year)


#가격 분포 시각화 
#1. 가격 분포 히스토그램
plt.hist(books_df['가격'], bins=20, color='skyblue', edgecolor='black')
plt.title('가격 분포')

plt.xlabel('가격 (원)')
plt.ylabel('도서 수')
plt.show()

#2. 출판년도별 도서 수 막대그래프
books_by_year.plot(kind='bar', color='salmon', edgecolor='black')
plt.title('출판 연도별 도서 수')
plt.xlabel('출판 연도')
plt.ylabel('도서 수')
plt.show()