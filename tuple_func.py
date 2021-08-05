list = [1,2,3,4,5]
for i, v in enumerate(list):
    print("{}번째 값:{}".format(i,v))
    
for a in enumerate(list):
    print("{}번째 값:{}".format(a[0],a[1]))
    
for a in enumerate(list):
    print("{}번째 값:{}".format(*a))
    
ages = {"Tod":35,"Jane":23,"Paul":62}

for a in ages.items():
    print("{}는 {}살이다".format(a[0],a[1]))
    print("{}는 {}살이다".format(*a))