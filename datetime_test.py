#datetime : 날짜와 시간을 사용하게 해주는 라이브러리
import datetime
print(datetime.datetime.now())
# 년, 월 , 일, 시, 분, 초, 밀리초

start_time = datetime.datetime.now()
print(type(start_time))
print(start_time)

start_time = start_time.replace(year = 2017, month = 2, day = 1)
print(start_time)

start_time = datetime.datetime(2016,2,1)
print(start_time)

how_long = start_time - datetime.datetime.now()
print(type(how_long))

print(how_long)

#timedelta : 시간의 연산을 가능하게 해주는 클래스

hundred = datetime.timedelta(days = 100)
hundred_day = datetime.datetime.now()+hundred
print(hundred_day)
hundred_day = datetime.datetime.now()-hundred
print(hundred_day)

tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days = 1)
print(tomorrow)