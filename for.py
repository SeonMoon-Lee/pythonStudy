#for

patterns = ["가위","바위","보"]
for pattern in patterns:
    print(pattern)
    
#for Range
#필요한 만큼의 숫자를 만들어내는 유용한 기능
for i in range(10):
    print(i)
    
names = ["철수","영희","바둑","미생"]

for i in range(len(names)):
    name = names[i]
    print("{},{}".format(i+1,name))

#enumerate
#리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
for i, name in enumerate(names):
    print("{},{}".format(i+1,name))

for i in range(11172):
    print(chr(44032+i),end='')
