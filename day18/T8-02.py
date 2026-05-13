import uvicorn
from fastapi import FastAPI

#2.fastapi 객체 생성
app=FastAPI()

#3.서버 실행
if __name__=="__main__":
    uvicorn.run("T8-02:app",host="127.0.0.1",port=8000,reload=True)


#4.rest 정의하기
#rest:자원을 주고 받는 상태 구조
#자동으로 json 타입으로 응답한다. vsResponseBody(@RestController)
# @GetMapping() vs @app.get()
@app.get("/") #HTTP GET 방식으로 매핑시킨다.
async def index(): #async 동기 처리
    return "안녕 파이썬웹"


#5. 쿼리 파라미터
@app.get("/user")
async def find_user(name,age:int): #url?변수=값&변수명=값 #변수명:타입
    return {'name':name,'age':age} #기본타입 str #변수명 :타입


#6.경로 파라미터 #예 http://localhost:8000/item/유재석/25
@app.get("/item/{name}/{age}")
async def find_item(name:str,age:int):
    return{'name':name,'age':age,'msg':'경로파라미터예시'}

#7.본문(body)        #Post,put만 가능

@app.post("/product")
async def find_product(product:dict):   #변수명:dict,딕셔너리 형태
    return product
  
  
#restapi 테스트:talend api 사용
#restapi 테스트:[1] TalendAPI [2]postman #[3]fastapi docs
