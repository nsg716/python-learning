# if문의 필요성 : 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 게 쓰는 것이 바로 if 문이다. 
# if 문의 기본 구조 
""" 
if 조건문 :
    수행할 문장 1
    수행할 문장 2
else :
    수행할 문장 1
    수행할 문장 2

"""  # 조건문이 참이면 바로 if문을 실행하고, 거짓이면 else 문을 수행하게 된다. else는 독립적으로 사용이 불가능하다.

# 들여쓰기 
# if 조건문 : 바로 아래 수행할 모든 문장은 들여쓰기를 해아 한다.들여쓰기의 너비는 같아야 한다. 
# if 문 예시 
money = True
if money :
    print ('참')
# 들여쓰기를 할때는 스페이스를 쓰던지 탭을 쓰던지 하나만 써라

# 조건문
# 비교 연산자 
# x > y     x가 y보다 작다
# x < y     x가 y보다 크다
# x == y    x와 y가 같다
# x != y    x와 y같지 않다
# x >= y    x가 y보다 크거나 같다
# x <= y    x가 y보다 작거나 같다.
x = 3
y = 2
print (x > y)   # T
print (x < y)   # F
print (x == y)  # F
print (x != y)  # T
print (x >= y)  # T
print (x <= y)  # F
print()

# 예제1 : 만약 3000이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라 

money = 2000
if (money >= 3000) :
    print ("택시를 탄다.")
else :
    print("걸어간다.")

# and, or, not 
# x or y    x 와 y 둘 중 하나만 참이면 참이다.
# x and y    x 와 y 모두 참이면 참이다. 
# not x    x 가 거짓이면 참이다.  

#예제2 : 만약 3000이상의 돈을 가지고 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라 
money = 2000
card = True
if (money >= 3000 or card ) :
    print ("택시를 탄다.")
else :
    print("걸어간다.")
print()

## x in s, x not in s
# 파이썬만 가지고 있는 조건문이다. 
""" 
    in                not in
x in 리스트       x not in 리스트
x in 튜플         x not in 튜플
x in 문자열       x not in 문자열

in은 "~안에"라는 뜻이다. 
"""
# 예시
print (1 in [1,2,3])        # T
print (1 not in [1,2,3])    # F

print ('a' in {'a','b','c'})# T
print ('j' not in 'python') # T
print()

# 예제 3 : 만약 주머니에 돈이 있으면 택시를 타고 없으면 걸어가라 
pocket = ['paper','cellphone','money']
if ('money' in pocket) :
    print ("택시를 탄다.")
else :
    print("걸어간다.")
print()

# 조건문에서 아무 일도 하지 않게 설정하는 방법
# 예제 4 : 주머니에 돈이 있으면 가만히 있고, 없으면 카드를 꺼내라 
pocket = ['paper','cellphone','money']
if ('money' in pocket) :
   pass # pass가 실행되고 아무런 결과값을 보여주지 않는다. 

else :
    print("카드를 꺼낸다")
print() 

## 다양한 조건을 파악하는 elif 문 
# 조건을 판단하는 부분이 여러 부분일 경우 elif 문을 사용이 가능하다.
# 예제 5 : 주머니에 돈이 있으며 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라

# if 문과 else 만 사용 
pocket = ['papper','cellphone']
card = True
if 'money' in pocket :
    print ("택시를 탄다.")
else :
    if card : 
        print ("택시를 탄다.") 
    else :
        print ("걸어간다.")
print ()

# elif 사용 - elif 문은 이전 조건문이 거짓일때 수행된다. 개수에 제한이 없다.
pocket = ['papper','cellphone']
card = True

if 'money' in pocket :
    print ("택시를 탄다.")
elif card :
    print ("택시를 탄다.")
else :
    print ("걸어간다.")
print ()

# 예제 4 간략화 - : 뒤에 수행문을 적어두었다. 
pocket = ['paper','cellphone','money']
if ('money' in pocket) : pass # pass가 실행되고 아무런 결과값을 보여주지 않는다. 
else : print("카드를 꺼낸다")
print() 

# 조건부 표현식 
'''
if score >= 60 :
    meesage = "sucess"
else :
    message = "failure"

'''
# 이를 파이썬의 조건부 표현식(conditional experssion)을 사용하면 다음과 같다
"""
message = "sucess" if score >= 60 else "failure"

"""

# 조건부 표현식의 정의 : [조건문이 참인 경우] [if 조건문 else] [조건문이 거짓인 경우]  - 가독성이 좋고, 활용성이 좋다