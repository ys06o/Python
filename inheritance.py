#[9] 상속

class Parent:
    def __init__(self):
        self.value='테스트'
        print('부모 클래스의  생성자가 호출되었습니다.')
    def test(self):
        print('부모클래스의 test() 메소드입니다.')


class Child(Parent): #class 클래스명(상위클래스명)
    def __init__(self):
        super().__init__() #부모의 생성자를 호출한다
        print('자식 클래스의 생성자가 호출 되었습니다.')
        
      
child=Child()  #상속된 인스턴스가 생성될 때:자식이 생성되면 부모도 자동으로 생성된다.
child.test()
print(child.value) #자식은 부모의 멤버변수와 멤버함수를 사용할 수 있다 ->상속받음,부모에게 물려받음


#[10]상속을 이용한 customException 만들기

class CustomException(Exception): #Exception 클래스로 부터 상속을 받는다.
    def __init__(self,message,value):
        super().__init__()
        self.message=message
        self.value=value
        
    #오버라이드
    def __str__(self):
        return self.message
    
    def print(self):
        print('## 오류 정보')
        print('메세지:',self.message)
        print('값:',self.value)


#강제로 예외 발생시키기

try:
    raise CustomException('강제로 예외 발생시키기',10)
except CustomException as e:
    print(e)
    e.print()