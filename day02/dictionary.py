#딕셔너리 란? 키를 기반으로 값을 저장하는 것
#json ,map이란 같은 개념

#[1] 선언 {"키 ":"값"}
dict_a={"name":"어벤져스 엔드게임","type":"히어로 무비"}
#[2] 호출
print(dict_a)
#[3] 특정한 값 호출
print(dict_a["name"])
print(dict_a.get("name")) #java map처럼 호출 가능  .get가능
print(dict_a["not"]) #keyerror발생 존재하지 않는 키는 오류발생

#[3] 딕셔너리 값 추가하기 ,딕셔너리 명['key']=value
dict_a["price"]=1000
print(dict_a)
dict_a['price']=20000 # 만약에 존재하는 키이면 value값이 수정됨
print(dict_a)

#[4]딕셔너리 키 /값 제거하기 del 딕셔너리 명 삭제할 키
del dict_a["price"]
print(dict_a)


#반복문과 딕셔너리 관계
# for 키 in 딕셔너리명:

for key in dict_a:
  print(key,dict_a[key])


dict_a={}
dict_a['name']='구름'
print(dict_a)

dict_a={"name":"구름"}
del dict_a["name"]
print(dict_a)

pet=[
  {"name":"구름","age":5},
  {"name":"구름1","age":2},
  {"name":"구름2","age":3},
  {"name":"구름3","age":5}
]

for key in pet:
    print(f'{key["name"]} {key["age"]}살')
  


numbers=[1,2,235,25,2,52,5612,66,315,155]
counter={}

for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1

print(counter)


#4번

character={
    "name":"기사",
    "level":12,

    "items":{
        "sword":"df",
        "sdsf":"df"
    },
    "skili":["dsf","sdf","qwe"]
}
for key in character:
    if type(character[key]) is dict: #딕셔너리 내 key값이 딕셔너리 이면
      for 요소 in character[key]:
         print(요소,character[key])
    elif type(character[key]) is list:
        for 요소 in character[key]:
          print(key,요소)
    else:
        print(key,character[key])    