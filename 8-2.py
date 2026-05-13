#isinstance(객체,클래스명), 만약에 해당 객체가 클래스로 만들어 졌다면? True,아니면 False

# vs 자바에서는? 객체 instance of 클래스명

#[1] 클래스 선언하기

class Student:
    count=0 #클래스변수 vs자바 static변수
    def study(self):
        print('공부를 합니다.')
    def __str__(self):
        return "학생"
    def __eq__(self, value): #==이 호출될떄 자동으로 실행되는 함수
        return 80==value
    
    def func1(self):
        return Student.count+1 #특정한 함수안에서도 클래스 변수 호출가능하다.
    #클래스 함수 vs static void~

    #@classmethod  #데코레이터를 사용한다. 파이썬에서는
    @classmethod
    def print(cls): #cls:class에 약자로 해당 클래스를 가르킨다.
        print('학생 목록')
        print('클래스 함수 호출')
        print(cls.count)
class Teacher:
    def teach(self): #str()함수가 호출될때 자동으로 실행되는 함수
        print('학생을 가르칩니다.')

#[2]인스턴스 생성
classroom=[Student(),Student(),Teacher(),Student(),Student()]

#[3]리스트내 인스턴스들의 타입을 확인하기

for person in classroom:
    if isinstance(person,Student):
        person.study()
    elif isinstance(person,Teacher):
        person.teach()

#str사용하기
print(str(classroom[0])) # 학생이라고 출력됨
print(classroom[0]== 90)
print(classroom[0]== 80)


#[5]#클래스 변수 호출 #클래스명.변수명()
print(Student.count) #클래스변수는 인스턴스 없이 호출 가능 #자바에서 static과 매우 유사
print(classroom[0].func1())

#[6] 클래스 함수 호출 #클래스명.함수명()
Student.print()

#self->인스턴스 ,cls->클래스 를 가르킨다.



#[6] 프라이빗 변수, __변수명 vsjava:private 변수명

import math

class Circle:
    def __init__(self,radius):
        self.__radius=radius  #프라이빗 변수에 매개변수 대입
    
    def get_circumference(self):
        return 2*math.pi*self.__radius #클래스 내부에서는 프라이빗 변수 사용가능
    
    def get_area(self):
        return math.pi*(self.__radius**2)
    
    #[8] getter,setter 프라이빗 변수를 외부에서 간접적으로 접근이 가능하게 해준다.
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self,value):
        self.__radius=value
        
Circle(10) #인스턴스 생성후 변수에 저장하지 않았으므로 GC가 자동으로 삭제
circle=Circle(10)
#print(circle.radius)    #AttributeError: 'Circle' object has no attribute '__radius'
#프라이빗 변수이므로 직접 호출시 오류 발생

print(circle.radius) #getter #10

circle.radius=20 #간접 접근 setter

print(circle.radius) #20



