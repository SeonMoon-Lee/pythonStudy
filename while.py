#while 조건 :
#   액션
#if문은 조건이 맞으면 한번만 실행
#while 반복문은 조건이 맞다면 계속 반복



selected = None
while selected not in ['가위','바위','보']:
    selected = input('가위, 바위, 보 중에 선택하세요 >')
    
print("선택된 값은 : ",selected)

patterns = ['가위','바위','보'];
for pattern in patterns:
    print(pattern)
    
for i in range(len(patterns)):
    print(patterns[i])
    
length = len(patterns)
while i < length:
    print(patterns[i])
    i=i+1


        

