'''
사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
파일을 하나 만들어 예외를 정의
Exception 클래스를 상속받아 만든다.
'''

class UnexpectedRSPValue(Exception):
    '''가위 바위 보 가운데 하나가 아닌 값인 경우에 발생하는 에러'''
    
value = "가"

try:
    if value not in ["가위","바위","보"]:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("오류 발생")

def sign_up( ):
    ''' 회원 가입 함수 '''

try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")