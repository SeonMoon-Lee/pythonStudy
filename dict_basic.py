'''
Dictionary
여러값을 저장해두고 필요한 값을 꺼내 쓰는 기능
이름표를 이용하여 값을 꺼내 사용
사용할 때는 리스트와 비슷한 방식
딕셔너리명 = {
    이름:값
    }
'''

wintable={
"가위":"보",
"바위":"가위",
"보":"바위"
}

print(wintable["가위"])

def rsp(mine,yours) :
    if mine == yours:
        return "draw"
    elif wintable[mine] == yours:
        return "win"
    else:
        return "lose"

result = rsp("가위","바위")
print(result)

messages = {
"win":"이겼다!",
"lose" : "졌어...",
"draw" : "비깃다"}

print(messages[result])

dict = {"one":1,"two":2}

print(dict)
#값 변경
dict["one"] = 11

print (dict)
#추가
dict["three"] = 3

print(dict)
#제거
del(dict["one"])

print(dict)
#꺼내기 및 제거
value = dict.pop("two")

print(value)
print(dict)

ages = {"Tod":35,"Jane":23,"Paul":62}
print(ages)
for key in ages.keys():
    print("{}가 {}살이다".format(key,ages[key]))

for key,value in ages.items():
    print("{}는 {}살이다".format(key,value))
