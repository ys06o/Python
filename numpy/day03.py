import numpy as np

#1차원 배열 통계
x=np.array([1,2,3,4,5])

print(np.min(x))  #최솟값 출력
print(np.max(x))  #최댓값 출력
print(np.sum(x))  #배열 합 출력
print(np.argmin(x)) #최솟값의 위치를 출력
print(np.argmax(x)) #최댓값의 위치를 출력
print(np.ptp(x))    #최댓값-최솟값
print(np.mean(x))  #평균값 출력
print(np.median(x)) #중앙값 출력
print(np.var(x))   #분산값 출력 분산이란? 요소들의 흩어진 정도
print(np.std(x)) #표준편차 출력 표준편차란? 분산의 양의 제곱근
print(np.sqrt(x)) #루트


#사분위수:구역을 4개 구역으로 나눠서 데이터 분포 위치를 파악
q1=np.percentile(x,25) #1/4 25% 하위 25%
q3=np.percentile(x,75) #3/4 75% 하위 75%
print(q1)
print(q3)

q2=np.percentile(x,50) # 50% 중앙값
print(q2)

q4=q3-q1        
print(q4)


#2차원 배열 통계
y=np.array([[1,2,3],[4,5,6]])
print(y)
print(np.min(y))
print(np.min(y,axis=0)) #열 기준 최솟값 출력
print(np.min(y,axis=1)) #행 기준 최솟값 출력
print(np.max(y,axis=0))
print(np.sum(y,axis=0))
print(np.sum(y,axis=1))
print(np.mean(y)) #평균
print(np.argmax(y)) #최댓값의 위치를 출력
print(np.argmin(y))
print(np.median(y)) #중앙값
print(np.var(y))
print(np.std(y))