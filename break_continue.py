#break 반복문을 종료하는 명령어
#continue 반복문에서 해당 명령어 다음 코드를 실행하지 않고 돌아가는 명령어

list = [1,2,3,4,5,6,8,2,401894]
for val in list:
    if val % 3 == 0:
        print(val)
        break
        
for i in range(10):
    if i%2 ==0:
        continue
    print(i)