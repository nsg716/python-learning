# 함수가 사용되는 이유 : 반복적으로 사용되는 가치있는 부분 -> 어떤 입력값을 넣어서 어떤 출력값을 돌려준다.
# 파이썬 함수의 구조 
"""
def 함수 이름 (매개 변수 ):
    수행할 문장1 
    수행할 문장2 

"""
# def 는 람수를 만들때 사용하는 예약어이며, 람수 이름은 함수를 만드는 사람이 임의로 정할 수 있다. 
# 함수 예시 
def add (a,b):
    return a+b 
#  풀이 : 이 함수의 이름(함수 이름)은 add이고, 입력으로 2개의 값을 받으며, 결괏값은 두개의 입력값을 더한 값이다. 

# add  함수 사용 
a1 = 3
b1 = 4 
c = add (a1,b1)
print (c) 
# c에 add 함수의 결과를 대입하고 이를 확인하는 것이다. 
print()

# 매개변수(parameter)와 인수(arugmemnts)
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수 
# 인수는 함수를 호출할때, 전달하는 입력값을 의미한다.

"""
def add (a,b): - a,b 는 매개변수
    return a+b 

print (add(3,4)) - 3,4 는 인수
"""

# 입력값과 결괏값에 따른 함수의 형태 
# 일반적인 함수 
"""
def 함수 이름 (매개변수) : 
    수행할 문장 

    return 결과값 :

"""

# 일반적인 함수의 예시 
def add (a,b) : 
    result  = a + b
    return result # a+b의 결괏값 반환
a = add(3,4)
print (a)
# 입력값과 결괏값이 있는 함수의 사용법을 정리
"""
결괏값을 받을 변수 = 함수 이름 (입력 인수 1, 입력 인수 2, ...)

"""
print ()

# 입력값이 없는 함수 
def say () :
    return "Hi"
print (say()) 
# 입력값이 없는 함수는 () 안에 아무런 값도 넗지 않아야 한다. 

"""
결괏값을 받을 변수 = 함수 이름 ()

"""
print ()


# 결괏값이 없는 함수 
def add1 (a,b) : 
    print ("%d, %d의 합은 %d 입니다." % (a,b,a+b))

add1(3,4)
"""
함수 이름 (입력 인수1,입력 인수2 )
"""

# 결과값이 없다는 것을 확인 
a = add1(3,4) # 7
print(a)  # None
print ()

# 입력값도 결괏값도 없는 함수 
def say() :
    print ("Hi")
say()
print ()

"""
함수 이름 ()
"""

# 매개 변수를 지정하여 호출하기 - 순서에 상관없이 사용할 수 있다는 장점이 있다.  
result1 = add (a=3, b=7) 
result2 = add (b=5, a=3) 
print (result1, result2) 
print ()

# 입력값이 몇개가 될지 모르는 경우
"""
def 함수 이름 (*매개변수) - 매개변수 부분을 *매개변수로 바꾸면 된다. 
    수행할 문장 
"""
# 여러개의 입력값을 받는 함수 구하기 
def add_many (*args) : 
    result = 0
    for i in args :
        result = result + i 
    return result
# *args 는 임의의 이름이다. 아무 이름이나 써도 상관이 없다. 
print (add_many(1,2,3,4,5,6))
print ()


# 여러 개의 입력을 처리할 때, 다양한 매개변수 사용법 
def add_mul(choice, *args) : 
    if choice == "add" : # 매개변수 choice 에 "add" 를 입력받았을 때
        result = 0
        for i in args : 
            result = result + i 
    elif choice == "mul" : # 매개변수 choice 에 "mul" 를 입력받았을 때
        result = 1
        for i in args :
            result = result * i   
    return result
print(add_mul ("add",1,2,3,4,5)) 
print(add_mul ("mul",1,2,3,4,5))  

print ()

# 키워드 파라미터 - (딕셔너리 만들기) (매개변수에 **입력)
def print_kwargs(**kargs) :
    print(kargs)
print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3 )
print ()

# 함수의 결괏값은 언제나 하나이다. 
def add_and_mul (a,b) : 
    return a+b,a*b  # 2개의 매개변수를 받아 더한 값과 곲한 값을 돌려준다. 
print (add_and_mul(3,4)) # 1개의 결괏값이므로 결괏값의 형태는 튜플이다. 
# 튜플의 값을 2개의 결괏값을 받고 싶으면 다음과 같이 함수를 호출을 하면 된다. 
result1,result2 = add_and_mul(3,4)

# return이 2개일 경우 : return을 만나면 함수를 빠져나가서 return a*b 는 의미가 없다. 
def add_and_mul1 (a,b) : 
    return a+b,
    return a*b # 의미가 없음

# 매게변수 초기값 미리 설정하기 
def say_myself (name, old, man=True):
    print ("나의 이름은 %s 입니다." % name)
    print ("나의 나이는 %d 살입니다." % old)
    if man :
        print("남자입니다.")
    else :
        print ("여자입니다.")
say_myself("박응용",27) # 매개변수가 없지만 True 값을 가지게 된다. 
say_myself("박응용",27,True) # 둘다 같은 값을 표시한다.
say_myself("박응용",27,False) # 매개 변수가 다르면 출력된 값이 다르다.
print ()
"""

def say_myself (name, man=True,old):
    print ("나의 이름은 %s 입니다." % name)
    print ("나의 나이는 %d 살입니다." % old)
    if man :
        print("남자입니다.")
    else :
        print ("여자입니다.")
        
""" # 오류 : 초기값을 설정한 매개변수가 끝에 없으면 알맞는 변수에 입력되지 않는다. 따라서 초기화 하고 싶은 매개변수를 항상 뒤쪽에 놓아야 한다.


# 함수 안에서 선언한 변수의 효력 범위 
"""
실습1. vartest.py
실습2. vartest_error.py

"""
# 함수 안에서 함수 밖의 변수를 변경하는 방법 
# 1. return 사용하기 

# vartest_return.py
a = 1
def vartest (a):
    a = a + 1
    return a

a = vartest(a) # vartest(a)의 결괏값을 함수 밖의 변수 a에 대입 
print (a)  
# 함수 안의 a의 매개변수와 함수 밖의 매개변수는 다른 것이다. 
# 2. global 사용하기  
# vartest_global.py
a = 1
def vartest(): # global 매개변수는 함수의 매개변수 입력 불가 
    global a
    a = a + 1

vartest()
print(a) 
# global 함수는 사용하지 않는 것이 좋다. 함수는 독립적인것이 좋기 때문이다. 외부 변수에 종속되면 개발할 때 경우의수가 증가하기 때문이다. 
print ()


#lambda - def 함수와 동일한 역할을 한다. 함수를 한 줄로 간단하게 작성할 때 사용 한다. 
"""
lambda 매개변수 1, 매개변수 2 : 매개변수를 사용한 표현식 

"""
# 예시 
add = lambda a, b : a+b
result = add(3,4)
print (result)

# 아래에 있는 def를 사용한 함수와 동일하다.
def add(a,b) : 
    return a+b
result = add (3,4)
print (result)
    
