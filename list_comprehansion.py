'''
list comprehansion
리스트를 생성과 동시에 반복적으로 조건에 만족하는 값을 할당
'''

areas = []
for i in range(1,11):
    if i%2 == 0:
        areas = areas+[i*i]
    
print("areas ",areas)

areas2 = [i*i for i in range(1,11) if i%2 == 0]
print("areas2 ",areas2)

