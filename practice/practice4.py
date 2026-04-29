
import numpy as np

# CSV 파일 로드 (헤더 제외, 콤마 구분)

data = np.genfromtxt('./customer_purchase_data.csv', delimiter=',', skip_header=1)

# 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]

print(f"데이터 형태: {data.shape}")
id=data[:,0]
sales=data[:,4]
print(sales)
sum=np.sum(sales)
avg=np.mean(sales)
print(f"총 매출액:{int(sum)}원,평균 구매 금액{int(avg)}원")

visit=data[:,1]
result2=id[(visit>=20)|(sales>=2000)]
print(f"충성고객들:{result2}")




result3=np.mean(sales//visit)
print("방문당 평균매출:{}원".format(int(result3)))
#방문당 평균매출이 가장 높은 고객의 ID 출력
result4=np.argmax(result3)
print("방문당 평균매출이 가장 높은 고객의 ID:{}".format(int(id[result4])))


cart_items=data[:,3]

result5=id[(visit<=3)&(cart_items<=1)]
print(result5)

print("이탈 위험 고객{} 총{}명".format(result5,len(result5)))




#구매 금액 데이터를 0과 1사이의 정규화(min,max)
#정규화((값-최솟값)/(최댓값-최솟값))
#어떠한 자료들을 0과 1사이값으로 만들어서
#백분율 비교가 용이해진다.
data_min=np.min(sales)
print(data_min)
data_max=np.max(sales)
print(data_max)
print((sales-data_min)/(data_max-data_min))

norm_data=(sales-data_min)/(data_max-data_min)
vip=norm_data>=0.9
print(vip)
print('vip 고객님들 명단\n:',data[vip])


#-------------------------#
x=np.array([True,False,True])
y=np.array([1,2,3])
print(y[x])