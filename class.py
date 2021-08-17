class Human():
    '''인간'''
#person = Human()
#person.name = '철수'
#person.weight = 60.5

def create_human(name,weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human

person = Human.create("철수",60.5)

def eat(person):
    person.weight+=0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(person.name,person.weight))
    
def walk(person):
    person.weight-=0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(person.name,person.weight))
    
Human.eat = eat
Human.walk = walk

person.walk()
person.eat()


'''
class Human():
    """사람"""
    
person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

print(person1.language)
print(person2.language)

person1.name = "서울시민"
person2.name = "인도인"

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name,person.language))

speak(person1)
speak(person2)

Human.speak = speak

person1.speak()
person2.speak()
'''
