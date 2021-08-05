#모듈
#미리 만들어지 코드를 가져와 쓰는 방법
#import 모듈이름

import urllib.request
def get_web(url):
    response = urllib.request.urlopen(url) 
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input("웹 페이지 주소? ")
content = get_web(url)
print(content)