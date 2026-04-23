#콜백 함수:함수의 매개변수에 사용하는 함수

#콜백함수 예시 : 
def call_10_items(func): #매개변수를 함수로 받는 함수
  for i in range(10):
    func()

def print_hello():
    print("안녕하세요")

call_10_items(print_hello)   #함수자체 전달
# call_10_items(print_hello()) #함수실행 #예외 발생

#map,filter 함수
# map(함수,리스트): 리스트에 요소를 하나씩 함수매개변수에 대입하여 새로운 리스트 반환
#filter (함수,리스트) :리스트에 요소를 *하나씩* 매개변수에 대입하여 참인경우 새로운리스트를 반환


def power(item):
    return item*item

def under_3(item):
    return item<3


list_input_a=[1,2,3,4,5]

output_a=map(power,list_input_a)
print(list(output_a))      
output_b=filter(under_3,list_input_a)
print(list(output_b))

      #while(rs.next()) jdbc에서 레코드 1개씩 순회할떄 비슷하다




#람다:함수 선언을 간단하게 하는 문법
#lamda 매개변수:반환값
#방법1: 람다를 변수로 만듬 ,재사용 가능
power=lambda x:x*x
list_input_a=[1,2,3,4,5]
output_a=map(power,list_input_a)
#방법2:바로 map에 람다식을 넣는다. 단점:재사용이 안된다.
output_a=map(lambda x:x*x,list_input_a)
print(list(output_a))


