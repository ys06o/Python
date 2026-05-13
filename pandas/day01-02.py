import pandas as pd

#판다스
#pd.Series :1차원
#pd.DataFrame :2차원

#[1] 데이터프레임 생성 1 (2차원 리스트 형태로)
data_list=[ #2차원 리스트 pd.DataFrame(2차원리스트,coulmns=[열이름목록])
  ['ant',25,'seoul'],
  ['bee',30,'busan'],
  ['cat',35,'incheon']
  ]
x=pd.DataFrame(data_list,columns=['name','age','city'])
print(x)

#[2]데이터프레임 생성 2 (딕셔너리 형태로) #대부분의 공공자료는 딕셔너리 형태이다.
data_dict={'name':['ant','bee','cat'],'age':[25,30,35],'city':['seoul','busan','incheon']}
print(pd.DataFrame(data_dict))


#[3]데이터프레임 생성3, pd.DataFrame(넘파이배열,columns=[열이름])
import numpy as np
data_np=np.array(data_list)
x=pd.DataFrame(data_np,columns=['name','age','city'],index=['a','b','c'])

#[4] 주요 속성
print(x.shape) #행열 크기 (3,3)
print(x.columns) #컬럼 목록
print(x.index) #인덱스 행 목록
print(x.values) #값만 2차원 으로 반환

#[5] 주요 탐색
print(x.head(2))  #상위 n개만 반환
print(x.tail(2)) #하위 n개만 반환
print(x.info())  #전처리 (데이터 정리) 하기전에 결측치 확인

#[6] 인덱싱
print(x.iloc[1]) #iloc[인덱스번호]
print(x.iloc[1,2]) #iloc[행,열]
print(x.loc['b'])
print(x.loc['b','city'])

#[6] 슬라이싱
print(x.iloc[0:2,0:1])
print(x.loc['a':'b','name':'city'] ) 

#[7] 새로운 열 추갸
x['score2']=[100,15,21] #값이
print(x)

#[8]특정한 값 숮ㅇ
x['age']=[32,23,11]
print(x)

x.loc['b','age']=70
print(x)
x.iloc[0,0]='apple'


#여러개 한번에 수정,loc[시작라벨:끝라벨,컬럼라벨]

x.loc['a':'b','score']=[10,20]
print(x)

#[9]필터링 ,x[조건식],x[x[열이름>논리식]]
print(x['score2']>70)
con1=x['score2']>70
print(x[con1])

con2=x['age']>35 #두번째 조건
print(x[con1|con2])

#[10] 필터링 조건으로 새로운 열 추가 또는 수정
x.loc[x['score2']>70,'passed']=True  
print(x)
x.loc[x['score2'] <=70,'passed']=False
print(x)


#[11] 열(컬럼) 이름 수정, .rename(index={},columns{'old:new})
x=x.rename(columns={'city':'도시','name':'이름'})
print(x)

#[12] 집계 .descirbe():수치 자료들을 집계 요약 :문자 제외 ,
print(x.describe())
print(x['age'].sum())
print(x['score'].mean())

print(x['passed'].value_counts) # 특정열의 빈도 확인


