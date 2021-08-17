'''
오버라이드
같은 이름을 가진 메소드를 덮어 쓴다는 의미
'''

class Animal():
    def walk(self):
        print("걷는다")
    def eat(self):
        print("먹는다")
    def great(self):
        print("인사한다")
class Cow(Animal):
    '''소'''

class Human(Animal):  
    def wave(self):
        print("손을 흔든다")
    def great(self):
        self.wave()
    
class Dog(Animal):
    def wag(self):
        print("꼬리를 흔든다")
    def great(self):
        self.wag()
        
        
person = Human()
person.great()

dog = Dog()
dog.great()

cow = Cow()
cow.great()