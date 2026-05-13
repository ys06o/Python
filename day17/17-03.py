#동적페이지 크롤링
#웹페이지 자료가  js에 의해 대기 상태있는 경우(js통신)


#[1] 설치 pip install playwright #파이썬 라이브러리
#playwright install #브라우저 설치

import asyncio #비동기 라이브러리
from playwright.async_api import async_playwright 
#동적페이지 크롤링 라이브러리
import pandas as pd

#[3] 크롤링 주소 확인 https://search.naver.com/search.naver?l&where=image&query=%EC%A7%B1%EA%B5%AC



#[4]비동기 웹크롤링
async def naverRun(): #동기화된 함수
    #(1)playwright 실행하고 p 변수에 결과를 대입하기
    async with async_playwright() as p:
      #(2) await(대기) 상태를 이요한 크롬 실행
      browser=await p.chromium.launch(headless=False)
      #headless=False 브라우저가 직접 실행된다. 봇 차단방지
      #(3)실행된 브라우저에서 새로운 페이지에 지정된 url 대입하여 이동
      url='https://search.naver.com/search.naver?l&where=image&query=짱구'
      page= await browser.new_page() #url
      await page.goto(url) #새로운 탭 열기
      
      #(4-1) (자료가 표시될 때 까지 기다리기)대기상태 만들기
      #(4-2)스크롤 내리기 이벤트(js):
      
      for i in range(2): #스크롤 두번내리기
          await page.wait_for_timeout(3000)
          #window(브라우저).scrollTo(시작,이동위치)
          #이동위치:document(현재html).body(본문).scrollHeight(스크롤높이) :즉 현재 브라우저 스크롤을 본문의 가장 하단으로 이동
          await page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
      # page.wait_for_timeout(밀리초):시스템에 따라 적절하기 사용하기
      await page.wait_for_timeout(2000)
      #(5)실행된 페이지에서 특정한 요소가져오기
#박스:tile_item, 이미지:_fe_image_tab_content_thumbnail_image
#제목:info_title
      # page.query_selector_all(식별자)
      items=await page.query_selector_all('.tile_item')
    
      image_list=[]
      for item in items: #여러개 item에서 제목과 이미지 가져오기
        title_tag=await item.query_selector('.info_title .txt') #제목
        image_title=await title_tag.inner_text() if title_tag else '제목없음'#<> inner_text <>

        image_tag=await item.query_selector('.img_fe_image_tab_content_thumbnail_image')#이미지
        image_link=await image_tag.get_attribute('src') if image_tag else '제목없음' #get_attribute('속성명')

        image_list.append({'제목':image_title,'링크':image_link}) #리스트에 넣기
    
    
      print(image_list)
      #(6)안전하게 브라우저 닫기
      await browser.close()
asyncio.run(naverRun()) #동기화된 함수 실행