# 좀 더 다양한 입력과 출력에 대해 알아보자
# 사용자 입력
# input 의 활용 
a = input () # 사용자가 입력한 문장을 a에 대입 
print (a)

# 프롬프트 값을 띄어서 사용자 입력받기 
"""
input ("질문내용 : ")
"""
# 예시 
number = input("숫자를 입력하시오 : ")
print (number)
print ()

# print 자세히 알기 
a = 123 
print (a) # 숫자 출력하기 
a = "Python"
print (a) # 문자열 출력하기 
a = [1,2,3]
print (a) # 리스트 출력하기 
print ()

# 큰따음표("")로 둘러싼인 문자열은 + 연산자와 동일하다 
print ("Life""is""too short")
print ("Life"+"is"+"too short") # 위와 동일하다

# 문자열 띄어쓰기는 콤마(,)로 한다.
print ("Life","is","too short")

# 한줄에 결괏값 출력하기 - 매개변수 end를 사용해 끝 문자를 지정해야한다.
for i in range(1,10) :
    print (i, end = " ")

