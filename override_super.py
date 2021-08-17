'''
Super
부모클래스의 내용을 사용 할 수 있다.
super()
'''

class Animal():
    def __init__(self,name):
        self.name = name

    def walk(self):
        print("걷는다")
    def eat(self):
        print("먹는다")
    def great(self):
        print("{}이(가) 인사한다".format(self.name))

class Human(Animal):  
    
    def __init__(self,name,hand):
        super().__init__(name)
        self.hand = hand
    
    def wave(self):
        print("{}을 흔들면서".format(self.hand))
    def great(self):
        self.wave()
        super().great()

        
        
person = Human("사람","오른손")
person.great()
