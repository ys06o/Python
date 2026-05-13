import asyncio
from playwright.async_api import async_playwright
import pandas as pd

#[1] 크롤링 웹페이지
#https://web.joongna.com/search/코카콜라?page=1

#[2] 동기화 함수 ,async def 함수명()
async def webRun():
    #[3] 브라우저 실행
    async with async_playwright() as p:
      browser=await p.chromium.launch(headless=False)
      page=await browser.new_page()
    
    #[4]크롤링할 페이지로 이동
      await page.goto('https://web.joongna.com/search/코카콜라?page=1')
    #[5]해당 페이지가 모두 열렸을때까지 대기,시스템상태를 알수가 없을때 사용
    
    #[5-1]특정한 검색창 활용
      await page.get_by_placeholder('최소 가격').fill('10000') #최소가격 입력상자에 10000대입
      await page.wait_for_timeout(500)
      
      await page.get_by_placeholder('최대 가격').fill('20000')
      await page.wait_for_timeout(1000)
      
      #버튼 클릭 이벤트 특정한 식별자가 없는경우에 버튼에 보이는 이름으로 가져 올 수 있다.
      
      button=page.get_by_role('button',name='적용')
      await button.click()
      await page.wait_for_timeout(3000)
      
      
      await page.wait_for_load_state('networkidle') #통신이 모두 종료된 상태
    
    #[6]특정한 요소 가져오기
    #선택자:a[]
      items=await page.query_selector_all('div.group>div>a[href^="/product/"]')
      print(items)
      
      for item in items:
          title_tag=await item.query_selector('span.text-14')
          title=await title_tag.inner_text() if title_tag else '없음'
      
      #가격 가져오기
          price_tag=await item.query_selector('span.text-18')
          price=await price_tag.inner_text() if price_tag else 0
          print(title)
          print(price)     
            
#동기 함수 실행 동적페이지는 대기상태가 존재하기 때문에
#asyncio.run(동기함수())       

asyncio.run(webRun())