'''
메소드 : 클래스 내부 함수
특수 메소드 
__init__() : 인스턴스를 만들 때 실행되는 함수 (생성자)
__str__() : 인스턴스 자체를 출력할 때의 문자열 형식을 지정해 주는 함수
'''
class Human():
    '''인간'''
    def __init__(self,name,weight):
        #초기화 함수
        print("__init_실행")
        print("이름은 {},몸무게는 {}".format(name,weight))
        self.name = name
        self.weight = weight
        
    def __str__(self):
        #문자열화 함수
        return "{}(몸무게 {}kg)".format(self.name,self.weight)

    def eat(self):
        self.weight+=0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(person.name,person.weight))
    
    def walk(self):
        self.weight-=0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(person.name,person.weight))
    def speak(self, message):
        print(message)

person = Human("철수",60.5)

person.walk()
person.eat()

person.speak("안녕하세요")

print(person)