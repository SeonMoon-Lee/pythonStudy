#함수 
def function():
    print('안녕, 함수')
    
def print_root(a,b,c):
    r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    
    print('해는 {} 또는 {}'.format(r1,r2))

print()     #내장 함수
print()
print()
function()  #커스텀 함수

x=2
y=-6
z=-8
print_root(x,y,z)

def print_round(number):
    rounded = round(number)
    print(rounded)
    
print_round(4.6)
print_round(2.2)

def add_10(value):
    result = value+10
    return result
    
n = add_10(42)
print(n)