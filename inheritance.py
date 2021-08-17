'''
클래스간에 부모 자식 관계를 만들어서 
상속하는 클래스를 부모클래스
상속받는 클래스를 자식클래스
자식 클래스는 부모클래스의 함수나 변수를 사용할 수 있다.
'''

class Animal():
    def walk(self):
        print("걷는다")
    def eat(self):
        print("먹는다")

class Human(Animal):  
    def wave(self):
        print("손을 흔든다")
    
class Dog(Animal):
    def wag(self):
        print("꼬리를 흔든다")
        
        
person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()