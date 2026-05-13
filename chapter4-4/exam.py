#[1] min ,max , sum
numbers=[103,52,263,32,77]
print(max(numbers)) #최솟값
print(min(numbers)) #최댓값
print(sum(numbers)) #누적합계


#[2] reversed(리스트), 이터레이터가 반환된다.
print(reversed(numbers)) #<list_reverseiterator object at 0x000001E3C5706170>
print(list(reversed(numbers)))
for i in reversed(numbers):
  print(i)    #역순으로 출력이 된다.  77,32,263,52,103


#[3]enumerate(리스트) :인덱스와 자료를 순회가능
print(enumerate(numbers)) #<enumerate object at 0x000001E3C5975F80>
print(list(enumerate(numbers))) #[(0, 103), (1, 52), (2, 263), (3, 32), (4, 77)]

for index,value in enumerate(numbers): 
    print(index,value)



#[4] items()

example_dictionary={'키A':'값A','키B':'값B','키C':'값C'}

print(example_dictionary.items()) #dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])


for key,value in example_dictionary.items():
    print(key,value)



#[5]리스트내 반복문 사용,0부터 20 사이의 짝수를 갖는 리스트
#사용처:반복문을 이용한 리스트 생성할때

#방법 1
array=[]
for i in range(0,20,2):
    array.append(i)
    
print(array)


#방법 2 :표현식(계산식) for 반복변수 in 반복할수있는것 if 조건식:
array=[i for i in range(0,20,2)]

print(array)


array=[i for i in range(0,20,2) if i !=10] #10을 제외한 리스트 내포

print(array)




#[6]여러 줄 입력하기 
#(1) """"""
print("""
안녕하세요
안녕하세요2

"""
)

#(2) \n
print("안녕하세요1\n안녕하세요2")

#(3) ()소괄호 안에서 여러개 문자열 연결 가능
print(("안녕하세요\n" "안녕하세요2"))


#***********
#(4) 조합문자열.join(문자열리스트) ,리스트내 요소 사이에 조합문자열 연결을 해준다.
#csv할때 많이씀 알아둘것
print(   "\n".join(["안녕하세요1","안녕하세요2"]))




output=[i for i in range(1,101) if "{:b}".format(i).count('0')==1]

print(output)

for i in output:
    print("{}:{}".format(i,"{:b}".format(i)))

print("합계",sum(output))








