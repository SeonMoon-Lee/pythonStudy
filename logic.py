a = 10
if a<10 and 2**a > 1000 and a%5 == 2 and round(a) == a:
    print("복잡한 식") 
    
def return_false():
    print("함수 return false")
    return False
    
def return_true():
    print("함수 return true")
    return True

a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)
    
print("test 2")

#논리 연산중 앞부분부터 처리하고 더 이상 처리할 필요가 없을 경우 바로 if문을 빠져나간다.
if return_false() and return_true():
    print(True)
else:
    print(False)
    
#bool안에 0 이외에 모든 값이 true
#bool안에 빈 리스트를 넣으면 false
#bool안에 None, ''를 넣으면 false

value = input("입력해 주세요>") or "아무것도 못받았어"
print ("입력받은 값>",value)