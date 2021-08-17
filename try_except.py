text = "100%"
try:
    number = int(text)
except ValueError:
    print("{}는 숫자가 아니네요.".format(text))
    
def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print("{} 인덱스의 값을 가져올 수 없습니다.".format(index))
        
safe_pop_print([1,2,3],5)

try:
    import my_module12
except ImportError:
    print("모듈이 없습니다.")


'''
try:
    에러가 발생할 가능성이 있는 코드
except 에러종류:
또는 
except Exception as ex:
    에러가 발생 했을 경우 처리할 코드
    
if else로 처리할 수 있는것은 if else로 처리하는 것을 추천
'''