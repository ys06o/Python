import numpy as np

data = np.genfromtxt(
    './layoffs_events.csv',
    delimiter=',',
    encoding='utf-8',
    skip_header=1,
    dtype=str,
    invalid_raise=False # 불러오기 실패한 행은 제외
)
print(data.shape)


company=data[:,0]
ai_com=data[:,10]
layoff_count=data[:,2]
print(layoff_count)
x=np.where(layoff_count=="",'0',layoff_count)
print(company[ai_com=='True'])
