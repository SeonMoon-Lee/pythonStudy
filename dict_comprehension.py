'''
dictonary comprehension
딕셔너리를 생성과 동시에 값을 할당하는 문법
dict = { 키:값 for 키,값 in 반복돌릴것}
'''

students = ["태연","진우","정현","하늘","성진"]
for number , name in enumerate(students):
    print ("{}번의 이름은 {}입니다.".format(number,name))
    
students_dict = {"{}번".format(number+1): name for number, name in enumerate(students)}
print(students_dict)

scores = [85,92,78,90,100]
for x,y in zip(students, scores):
    print(x,y)
    
score_dict = {student:score for student, score in zip(students,scores)}
print(score_dict)