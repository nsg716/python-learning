# 파이썬으로 프로그래밍하기 위해 알아야 할 것들을 대부분 공부했다. 
# 이미 만들어진 것을 다시 만드는 것은 불필요한 행동이다. 
# 새로운 프로그램을 만들기 전에는 이미 만들어진 것들, 그 중에서도 특히 파이썬 라이브러리를 살펴보는 것이 중요하다.
# 활용빈도가 높고 중요한 함수를 중심으로 정리하였고, 순서는 알파벳 순서이다. 

# abs - 절댓값을 돌려주는 함수 
print(abs(3))
print(abs(-3))
print(abs(-1.2))
print ()

# all - 반복 가능한 자료형(리스트, 튜플, 문자열, 딕셔너리 등) x를 입력 인수로 받으며 이 x가 모두 참이면 True, 하나라도 거짓이면 False 이다.  
print (all([1,2,3]))
print (all([1,2,3,0]))
print ()

# any - any(x)는 x 중에 하나라도 참이 있으면 True, 전부 다 거짓이면 False (all의 반대)
print (any([1,2,3,0]))
print (any([0,""]))  # 리스트 자료형은 0과 "" 모두 거짓이다.
print ()

# chr - chr(i) 는 아스키 코드 값을 입력 받아 코드에 해당하는 문자를 출력하는 함수 
print (chr(97)) 
print (chr(48)) 
print ()

# dir - 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 다음 예는 리스트나 딕셔너리 객체 관련 함수를 보여주는 예이다.
print ("리스트 함수",dir([1,2,3]))
print ("딕셔너리 함수",dir({'1':'a'}))
print ()

# divmod - divmod(a,b) 는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 받는다. 
print (divmod(7,3))
print ()

# enumerate - 열거하다.라는 뜻 / 순서가 있는 자료형을 입력 받아 인덱스 값 (순서)을 포함하는 enumerate객체를 돌려준다. 
# 예시 
for i , name in enumerate(['body','foo','bar']) :
    print (i, name)
# 객체가 현제 어디에 있는지 알고자 할 때 유용하게 사용할 수 있다.
print ()

# eval - (experssion) 실행 가능한 문자열을 입력 받아 문자열을 실행한 결괏값으로 돌려주는 함수
print (eval('1+2'))
print (eval("'hi' + 'a'"))
print (eval('divmod(4,3)'))
print ()

# filter - 걸러낸다는 뜻 / 첫번째 인수로는 함수 이름을 두번째로 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
# 그리고 두번째 인수들을 첫번째 함수들에 넣었을 때 참인 것을 반환한다. 

"""
실습 1. : positive.py
실습 2. : filter.py
"""
# 간략화 버전 
print(list(filter(lambda x : x > 0, [1, -3, 2, 0 ,-5, 6])))
print()


# hex - 16진수 변환 
print (hex(234))
print (hex(3))
print ()

# id -  객체를 입력박아 고유 레퍼런스를 돌려주는 함수 
a = 3
b = a
print (id(3))
print (id(a))
print (id(b)) # 모두 같은 객체를 가리킨다. 
print (id(4)) # 다른 객체를 가리킨다.
print ()

""" 실습을 위해 주석처리 
# input - 사용자 입력을 받는 함수 
a = input ()
b = input ("Enter : ")
print (a)
print (b)
print ()
"""

# int  - 문자열 형태나 소수점이 있는 숫자를 정수형태로 변환, 정수는 정수 그대로 돌려준다. 
print (int('3')) # 문자열 
print (int(3.4)) # 소수점이 있는 숫자
# int (x ,radix)는 radix 진수로 표현된 문자열을 돌려준다.
print (int('11',2))
print (int('1A', 16))
print ()

# isinstance - isinstance(object, class)는 첫번째 인수로 인스턴스, 두번째 인수로 클래스를 받는다. 
# 입력받은 인스턴스가 참이면 True, 거짓이면 False 
class Person : pass
a = Person ()
print (isinstance (a, Person)) # a 가 Person의 인스턴스인지 확인 
b = 3
print (isinstance (b, Person)) # b 가 Person의 인스턴스인지 확인 
print ()

# len - 입력값의 길이 (요소의 전체 개수)를 돌려주는 함수이다. 
print (len("Python"))
print (len([1,2,3]))
print (len(( 1,'a')))
print ()

# list - 반복 가능한 자료형을 입력받아 리스트로 돌려주는 함수이다.
print (list("python"))
print (list((1,2,3)))
# 리스트를 받으면 그대로 돌려준다.
a = [1,2,3]
b = list(a)
print (b)
print ()

# map  - 반복 가능한 함수와 반복 가능한 자료형을 입력받아 입력 받은 자료형의 각 요소롤 함수가 수행한 결과를 묶어서 돌려준다. 
def two_times (numberList) :
    result = []
    for number in numberList :
        result.append(number*2) 
    return result
result = two_times([1,2,3,4])
print (result)
# map 함수 활용 
def two_times(x) : return x*2
print (list(map(two_times, [1,2,3,4]))) #  출력 결과를 보여주기 위해 list 로 출력
# lambda를 통해 간략화 
print (list(map(lambda a : a*2 , [1,2,3,4])))
print ()

# max - 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다. 
print (max([1,2,3]))
print (max("python"))
print ()

# min - max 함수와 반대로, 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
print (min([1,2,3]))
print (min("python"))
print ()

# oct - 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수 
print (oct(34))
print (oct(12345))
print ()

#open - open (filename, [mode])은 '파일 이름'과 ''읽기 방법'을 입력 받아 파일 객체를 돌려주는 함수 / 읽기 방법을 생략하면 읽기 전용 모드이다. 

"""
r : 읽기 모드
w : 쓰기 모드 
a : 추가 모드 
b : 바이너리 모드로 열기 

""" 

# f = open ("binary_file", "rb") - 바이너리 읽기 모드를 의미한다. 
# fread = open("read_mode.txt", "r") 
# fread2 = open ("read_mode.txt") - 위와 동일한 방법이다. 
# fappend = open("append_mode.txt" , "a")
# 실습을 위해서 주석 처리


# ord  -  문자의 아스키 코드를 돌려준다.
print (ord('a'))
print (ord('0'))
print ()

# pow - pow (x,y)은 x의 y제곰함 결괏값을 돌려주는 함수이다. 
print (pow(2,4))
print (pow(3,3))
print ()

# range - range([start,]stop[,step])는 for문과 함께 자주 사용하는 함수이다. 입력받은 숫자에 해당하는 범위값을 반복가능한 객체로 만든다.
# 인수가 하나일 경우 
print (list(range(5))) # 시작 숫자를 지정해주지 않으면 0부터 시작한다.
print (list(range(5,10)))
print (list(range(1,10,2))) # 세 번째 인수는 숫자 사이의 거리를 말한다. 
print (list(range(0,-10,-1)))
print ()

# round - 숫자를 입력받아 반올림해주는 함수
print (round(4.6))
print (round(4.2))
print (round(5.678,2)) # 두 번째 인수는 소수점 자리수 이다. 
print ()

# sorted -  입력한 값을 정렬한 후 리스트로 돌려준다. 
print (sorted([3,1,2]))
print (sorted(['a','c','b']))
print (sorted(["zero"]))
print (sorted([3,2,1]))
print ()

# str -  문자열 형태로 객체를 변환하여 돌려주는 함수이다. 
print (str(3))
print (str('hi'))
print (str('hi'.upper()))
print ()

# sum - 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다. 
print (sum([1,2,3]))
print (sum((4,5,6)))
print ()

# tuple - 반복가능한 자료형을 입력받아 튜플로 형태로 바꾸어 돌려주는 함수
print (tuple("abc"))
print (tuple([1,2,3]))
print (tuple((1,2,3)))
print ()

# type - 입력값의 자료형이 무엇인지 알려준다. 
print (type("abc"))
print (type([]))
# print (type(open("test",'w'))) 실습을 위해 주석처리
print ()

# zip - 동일한 개수로 이루어진 자료형을 묶어주는 역할의 함수이다. 
print (list(zip(([1,2,3],[4,5,6]))))
print (list(zip(([1,2,3],[4,5,6],[7,8,9]))))
print (list(zip("abc","def")))
