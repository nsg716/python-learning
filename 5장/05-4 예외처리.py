# 프로그램을 만들다 보면 수많은 오류를 만나게 되는데 try,except를 사용하여 오류를 무시하는 방법

# 오류 발생 원인 
# 디렉토리 안에 없는 파일을 열려고 할 때 
"""
f = open ("나 없는 파일" , "r") 
"""

# 0 으로 다른 숫자를 나눌 경우
"""
print (4/0)
"""

# 리스트에 얻을 수 없는 값 
"""
a = [1,2,3]
print (a[4])
"""

# 오류 예외 처리 기법 
# 문 
"""
try:
...
except [발생 오류 [as 오류 메시지 변수 ]]:
...

"""
# try 블록 수행중 오류 발생시 except 블록이 수행되며, try 블록에서 오류가 발생하지 않으면 except 블록은 수행되지 않는다.

"""
except 구문 
except [발생 오류 [as 오류 메시지 변수 ]]:

# 괄호는 생략이 가능하다 따라서 3가지 방법이 있다. 
"""

#1. try except 만 쓰는 방법 - 오류 종류에 상관업이 오류가 발생하면 except 블록을 수행한다. 
#2. 발생 오류만 포함시킨 except 문 - 오류가 발생했을 때 except문에 미리 정해놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 뜻이다. 
#3. 발생오류와 오류 메시지 변수까지 포함한 except문 - 오류 메세지의 내용까지 알고 싶을 때 사용한다. 

# 예시 
try :
    4 / 0
except ZeroDivisionError as e:
    print (e) # 결괏값 : division by zero
print()

# try ...finally - finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 주로 파일을 닫을 때 사용된다. 
# 예시 
f = open ("foo.txt",'w') 
try:
    4
    # 무언가를 수행한다.
finally :
    f.close()
# 여러개의 오류 처리하기 
# 예시 
try:
    a = [1,2]
    print(a[3]) # 인덱싱 오류가 먼저 발생해서 ZeroDivisionError 오류는 발생하지 않았다.   
    print(4/0)
except ZeroDivisionError : 
    print ("0으로 나눌 수 없습니다.")
except IndexError :
    print ("인덱싱할 수 없습니다.") 


print()
print ("-"*50)
print()


# 오류메세지 출력 (1개만 작동)
try:
    a = [1,2]
    print(a[3]) # 인덱싱 오류가 먼저 발생해서 ZeroDivisionError 오류는 발생하지 않았다.   
    print(4/0)
except ZeroDivisionError as e : 
    print (e)
except IndexError as e : 
    print (e) 


print()
print ("-"*50)
print()

# 오류 메시지 동시에 처리하기 
try:
    a = [1,2]
    print(a[3]) # 인덱싱 오류가 먼저 발생해서 ZeroDivisionError 오류는 발생하지 않았다.   
    print(4/0)
except (ZeroDivisionError,IndexError) as e : 
    print (e)

print ()

# 오류 회피하기 
try : 
    f = open ("나 없는 파일" , 'r')
except FileNotFoundError : # 파일이 없더라도 오류를 발생시키지 않고 통과한다.
    pass

# 오류 일부러 발생시키기 
# 프로그래밍을 하다보면 오류를 강데로 발생시켜애 할 경우도 있다.
# raise 명령어 

# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현하도록 만들고 싶은 경우가 있다.
# 예시 

class Bird:
    def fly (self):
        raise NotImplementedError
# fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 어떻게 될까?
"""
class Eagle(Bird) :
    pass
eagle = Eagle()
eagle.fly()
""" # 실습을 위해 주석 처리 
 #  Eagle 클래스는 Bird 클래스르 상속받는다. 그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 함수가 호출된다. 
 # 그리고 raise 문에 의하여 NotImplementedError 가 발생한다. 
 # 오류를 발생하지 않으려면 Eagle 클래스에 fly 함수를 반드시 구현해야 한다.



class Eagle(Bird) :
     def fly (self):
         print ("very fast")
eagle = Eagle()
eagle.fly()

print ()

# 예외 만들기 
# 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다. 
class MyError (Exception) :
    pass

# 별명을 출력해주는 함수 
def say_nick(nick) : 
    if nick == "바보" :
        raise MyError()
    print (nick)

# Say_nick 함수를 호출한다. 
say_nick("천사")
#say_nick("바보")  - 실습을 위해 주석 처리 

# 예외 처리 기법 사용 
try : 
    say_nick("천사")
    say_nick("바보")
except :
    print ("허용되지 않는 별명입니다. ")

print()

# 이동 

# 오류 메시지를 사용
try : 
    say_nick("천사")
    say_nick("바보")
except MyError as e :
   print (e) # 오류메시지가 보이지 않는다.


# 오류 메시지를 보이게 하려면 __str__ 메소드를 구현해야 한다. (이 부분을 위의 주석 이동에 순서를 넣어야 실습이 된다.)
class MyError (Exception) :
    def __str__ (self):
        return "허용되지 않는 별명입니다."



