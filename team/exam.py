import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import koreanfont                   # 한글폰트
import seaborn as sns               #seaborn
import json                         # JSON LOAD


df = pd.read_csv(
    './team/train_HousePrices.csv'                                    # 파일 경로
)
df.head()
df['LotFrontage']=df['LotFrontage'].fillna(df['LotFrontage'].median())
print(df.isnull().sum())
df['Alley'] = df['Alley'].fillna('NoAlley')
df['PoolQC'] = df['PoolQC'].fillna('NoPool')
df['Fence'] = df['Fence'].fillna('NoFence')
df['MiscFeature']=df['MiscFeature'].fillna('NoMiscFeature')


df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].median())
df.info()
df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].median())
df.info()
df['GarageYrBlt'] = df['GarageYrBlt'].fillna(df['GarageYrBlt'].median())
df.info()

df['Alley'] = df['Alley'].fillna('NoAlley')

df['PoolQC'] = df['PoolQC'].fillna('NoPool')

df['Fence'] = df['Fence'].fillna('NoFence')

df['MiscFeature'] = df['MiscFeature'].fillna('NoMisc')

fill_list = [
    "BsmtQual",
    "BsmtCond",
    "BsmtExposure",
    "BsmtFinType1",
    "BsmtFinType2",
    "Electrical",
    "FireplaceQu",
    "GarageType",
    "GarageFinish",
    "GarageQual",
    "GarageCond",
    "MSZoning",
    "Functional",
    "SaleType",
    "Exterior1st",
    "Exterior2nd",
    "MasVnrType"
    ]
for i in fill_list:
    df[i] = df[i].fillna(df[i].mode()[0])
df.info()

sns.histplot(df['SalePrice'],kde=True)
plt.title('주택 판매 가격 분포도')
plt.xlabel('판매 가격')
plt.ylabel('주택 수')

plt.show()


scatter=sns.scatterplot(
  data=df,x='SalePrice',y='GrLivArea'
)
scatter.set(
  xlabel='주택 판매 가격',
  ylabel='지상 주거 면적', 
  title='지상 주거 면적과 판매 가격 간의 상관관계'
)

plt.show()
