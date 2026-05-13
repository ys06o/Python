import uvicorn      #자바의 톰캣역할 #파이썬서버(8000)
from fastapi import FastAPI


#1.설치
#2.import uvicorn,from fastapi import FASTAPI
#3.자바와 다르게 파이썬은 인스턴스 생성시 new 없음
#4.uvicorn.run("파일명:app")
#5.서버 접속:http://localhost:8000,
#모듈 실행 시작점
app = FastAPI()
if __name__=="__main__":
    #uvicorn.run("파일명:app",host="현재 ip",port=서버포트,reload=자동재실행True) spring run과 같은 역할
    uvicorn.run("T8-01:app",host="127.0.0.1",port=8000,reload=True)


@app.get("/")
async def hello():
    return {"message": "Hello World"}