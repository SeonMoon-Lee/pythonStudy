list1 = ["가위","바위","보"]
list2 = [2,3,5,61,3,5,7]

print(list1)
print(list2)

print(list1[0])
print(list1[1])
print(list1[2])

list1[0] = "꽝"
print(list1[0])

print(list1[-1])
print(list1[-3])

list2.append(16)    #값 추가

print(list2)

list3 = list2+[16]  # 리스트 + 리스트

print(list3)

n = 12 
ownership = n in list3  #값 존재 유무 확인 bool

print(ownership)

n = 5
if n in list3:
    print("{}은 있어!".format(n))

del list3[1]    #1번째 값 삭제
print(list3)
list3.remove(5) #값 5 삭제
print(list3)

