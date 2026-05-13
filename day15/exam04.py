import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import team.koreanfont as koreanfont                   # 한글폰트
import seaborn as sns               #seaborn
import json                         # JSON LOAD

#캐글 :해외사이트 이면서 데이터셋 공유하는 사이트 ,데이터분석

import pandas as pd

df = pd.read_csv(
    './day15/train.csv'                                    # 파일 경로

)

print(df.head())
print(df.info())
print(df.isnull().sum())


# [1. 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster
# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 원칙)
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.
# [3. 자료수집 ]
# 3-1 : https://www.kaggle.com/competitions/titanic/overview
# 3-2 : train.csv 파일 판다스로 불러오기 
# [4. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# .fillna(채우기할 값) :만일 결측이면 특정값으로 채우기 함수
df['Age']=df['Age'].fillna(df['Age'].median())  #177
print(df.isnull().sum())
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0]) #2
print(df.isnull().sum())   
# [5. 데이터 시각화 및 분석]
# 5-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는  그래프 를 생성한다.
sns.countplot(data=df, x='Survived')
plt.xticks([0, 1], ['사망', '생존'])
plt.title('생존 분포')
plt.ylabel('인원수')
plt.show()
# 5-2 : 연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
#plt.bar:수치값 vs sns.countplot:범주값
# sns.countplot(data=df,x='라벨명(열이름)')
sns.countplot(data=df,x='Survived')  #x축 제목
plt.title('생존 여부 분포') #범주형 x축 레이블 수정
plt.xlabel('생존여부 0:사망 1생존') #y축 제목
plt.ylabel('인원 수')
plt.show()
print(df[df['Survived']==0]['Age'])

sns.histplot(df[df['Survived']==0]['Age'],label='사망',color='#ff0000',kde=True)
sns.histplot(df[df['Survived']==1]['Age'],label='생존',color='#0000ff',kde=True)

#KDE:커널밀도추정곡선: 막대 위에 부드러운 선
plt.title('나이별 생존 분포')
plt.xlabel('나이')
plt.ylabel('인원수')
plt.legend()
plt.show()
# 5-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
print(df['Sex'][0]) #male
sns.countplot(data=df,x='Sex',hue='Survived')
plt.title('성별 수')
plt.xlabel('성별')
plt.ylabel('인원수')
plt.legend(title='범례제목',labels=['사망','생존'])
plt.show()

# 5-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
print(df['Pclass'][0])
sns.countplot(data=df,x='Pclass',hue='Survived') #객실 등급 수
plt.show()
# 5-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data=df,x='Embarked') #승선 항구 수
plt.show()