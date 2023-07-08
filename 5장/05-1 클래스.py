# 클래스는 기존에 썻던 함수를 저장하는 역할이라고 생각하면 된다. (프로그램 틀)

# 클래스가 없는 더하기 
result = 0

def add5 (num):
    global result
    result += num 
    return result
print(add5(3))
print(add5(4))
print()

#  클래스가 없는 더하기 (계산식 2개 필요) - 각각의 계산식은 결괏값을 저장하기 때문에 함수를 2개 작성해야 한다.
result1 = 0
result2 = 0

def add1 (num):
    global result1
    result1 += num 
    return result1

def add2 (num):
    global result2
    result2 += num 
    return result2

print(add1(3))
print(add1(4))

print(add2(3))
print(add2(7))
print()

# 계산해야할 항목이 많아지면 추가할수는 있으나 점점 더 복잡해진다. 이를 해결하기 위한 것이 클래스이다. 

class Calculator: 
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# cal1, cal2 를 파이썬에서는 객체라고 부른다. 
# 계산기의 결괏값 역시 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지한다. 
# 클래스를 사용하면 객체를 생성만 하면 되기 때문에 함수를 사용라는 경우와 달리 매우 간단해진다.

# 빼기 기능 추가 
 
class Calculator: 
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
    def sub (self,num):
        self.result -= num
        return self.result

# 클래스와 객체 
# 클래스로 만든 객체의 특징 : 객체마다 고유한 성격을 가진다는 것이다. 

# 클래스의 가장 간단한 예시 - 과자 틀 
class Cookie :
    pass 
a = Cookie()
b = Cookie()
print ()
# a,b는 객체 
## 객체와 인스턴스의 차이
"""
클래스로 만든 객체를 인스턴스라고도 한다. 
인스턴스는 특정 객체가 어떤 클래스의 객체인지 관계를 설명할 때 사용한다.
a는 객체 , a는 Cookie 의 인스턴스 
"""
# 사칙연산 클래스 만들기 
# 클래스를 어떻게 만들지 먼저 구상하기 - 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할 것인지  미리 구상을 한 후 하나씩 해결하는 것 
# 그림을 그리는 것도 졸다.

# Fourcal - 사칙연산 클래스 
# 사칙연산을 하려면 두 숫자를 입력을 받아야 한다. - setdata메소드
# 나누기 기능은 ? - div 메소드 
# 빼기 기능은 ? - sub 메소드 
# 더하기 기능은 ? - add 메소드 
# 곱하기 기능은 ? - mul 메소드 

"""
1.먼저 객체를 만든다. 
    a = FourCal()
2. 숫자를 입력할 수 있는 메소드
    a.setdata(4,2)
3. 두수를 합한 결과 
    print(a.add())
4. 두수를 곱한 결과 
    print (a.mul())
5. 두수를 뺀 결과 
    print(a.sub())
6. 두수를 나눈 결과 
    print (a.div())
"""

# 클래스 구조 만들기 
# 클래스에서 객체 생성하기 
class FourCal : 
    pass # pass 는 아무것도 수행하지 않는 문법으로 임시로 코드를 작설할 때 주로 사용한다. 

a = FourCal()
print (type(a)) # a라는 객체 생성 

# 객체에 숫자 지정하기 
class FourCal : 
    def setdata(self, first, second) : # 메소드의 매개변수
        self.first = first  # 
        self.second = second # 매소드의 수행문
# 클래스 안에서 구현된 함수는 다른말로 메서드(Method, 메소드)라고 한다.  메소드도 일반 함수랑 다를 바가 없다. 

# 1. setdata 메소드의 매개변수 
"""
setdata는 3개의 매개변수를 입력받는다 여기서 self 는 setdata를 호출한 객체 a 가 자동으로 전달되기 때문이다. 
관례적으로 메소드의 첫번째 매개변수는 self를 사용한다. 객체를 호출할 때 자기자신이 호출되기 때문이다.

또 다른 호출방법으로는 메소드를 호출하는 벙법으로 가능하다.
a = FourCal()
클래스 이름.메소드 : FourCal.setdata(a,4,2)  - 호출할 때에는 첫번째 매개변수에 객체 a를 반드시 self에 전달해야 한다
객체.메소드 : a.setdata(4,2) - 호출 할 때, self를 반드시 생략해야 한다. 

"""

# 2. setdata 메소드의 수행문
"""
a.setdata(4,2)를 호출하면 
setdata 메소드의 매개변수 first,second에는 각각 값 4와 2 가 전달되어 setdata 메소드의 수행문은 다음과 같이 해석된다.
self.first = 4
self.second = 2

self는 객체 a 이므로 다음과 같이 해석된다.
a.first = 4 - a 객체에 객체변수 first 가 생성되고 4 가 저장된다.  
a. second = 2 - a 객체에 객체변수 second 가 생성되고 2 가 저장된다.  

"""
a =FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)
print()

# a, b 객체 만들기
a = FourCal()
b = FourCal()

a.setdata(4,2)
print(a.first)

b.setdata(3,7)
print(b.first)

print(a.first) # 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수와 상관없이 독립적인 값을 유지한다. (이 부분을 이해하는 것이 가장 중요)
print ()
# (여기까지 이해가 안된 부분이 있으면 다시 보기)

# 더하기 기능 만들기 
class FourCal : 
    def setdata(self, first, second) : 
        self.first = first  
        self.second = second
    def add (self):
        result = self.first + self.second
        return result
    
a = FourCal()
a.setdata(4,2)
print(a.add())

# add 메소드 분석하기 
"""
result = self.first + self.second 의 수행문을 가지는데 a.add가 입력되면서 이는  result = a.first + a.second이다. 
이때 a.add 호출 전에 a.setdata(4,2)가 호출되어 이는 result = 4+2 라고 해석된다. 

"""
print ()


# 곱하기, 빼기, 나누기 기능 만들기 
class FourCal : 
    def setdata(self, first, second) : 
        self.first = first  
        self.second = second
    def add (self):
        result = self.first + self.second
        return result
    def mul (self):
        result = self.first * self.second
        return result
    def sub (self):
        result = self.first - self.second
        return result
    def div (self):
        result = self.first / self.second
        return result
# 동작 확인하기 

a = FourCal()
b = FourCal()

a.setdata(4,2)
b.setdata(3,8)

print (a.add())
print (a.mul())
print (a.sub())
print (a.div())
print()

print (b.add())
print (b.mul())
print (b.sub())
print (b.div())
print ()

#생성자 (Constructor)

"""
a = FourCal()
print(a.add())

다음과 같이 실행했을 때,오류가 난다. 이는 FourCal클래스의 인스턴스 a에 setdata메소드를 수행하지 않고, 
add메소드를 수행하면 a.first,a.second의 객체변수가 없기 때문이다. 
이때문에 초기값을 설정을 할 필요가 있다.
"""
# 생성자라란 객체가 생성될 때 자동으로 호출되는 메소드를 의미한다. 
# 파이썬 메소들 이름으로 __init__를 사용하면 이 메소드는 생성자가 된다. 

# 클래스에 생성자 추가 
class FourCal : 
    def __init__(self,first,second) :
        self.first = first
        self.second = second
    def setdata(self, first, second) : 
        self.first = first  
        self.second = second
    def add (self):
        result = self.first + self.second
        return result
    def mul (self):
        result = self.first * self.second
        return result
    def sub (self):
        result = self.first - self.second
        return result
    def div (self):
        result = self.first / self.second
        return result

"""
a = FourCal () 를 수행하면 생성자의 first와 second에 해당되는 값이 전닿되지 않았기 때문에 오류 발생 
오류 해결 방법 
a = FourCal (4,2)

"""
# 생성자가 추가된 클래스
a = FourCal(4,2)
print (a.first)
print (a.second)
print (a.add())
print (a.div())
print ()

# 클래스와 상속 

# 상속은 '물려받다'라는 의미가 있다. 클래스에서 다른 클래스 기능을 물려받을 수 있게 만드는 것이다. 

# FourCal 클래스를 상속받는 MoreFourCal클래스 만들기 
class MoreFourCal(FourCal) :
    pass
""" 클래스를 상속하는 벙법
class 클래스 이름 (상속할 클래스 이름 )

"""
# MoreFourCal 는 Fourcal를 상속했으므로 FourCal클래스의 모든 기능을 사용할 수 있어야 한다.
a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print()

# 새로운 기능을 추가
class MoreFourCal(FourCal) :
    def pow(self): # a의 b 제곱을 계산
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
print(a.pow()) # 기능이 확장이 되었다. 
print()


# 메서드 오버라이딩 
"""
a = FourCal(4,0)
a.div()

실행을 하였을 때 나누기 값이 0은 나눌수가 없기 때문에 오류가 발생한다. 
오류가 아닌 0을 돌려주고 싶을 때 해결하는 방법

"""
class SafeFourCal(FourCal) :
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first/self.second
# 부모 클래스에 있는 것을 다시 만드는 것을 메소드 오버라이딩이라고 한다. 
# 메소드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메소드가 호츌된다. 

a = SafeFourCal(4,0)
print (a.div())
print ()

# 클래스 변수 - 클래스로 만든 모든 객체에 공유된다

class Family :
    lastname = "김"
# Family 클래스에 선언한 lastanme이 바로 클래스 변수이다.  클래수 변수는 클래스로 만든 모든 객체에 공유가 된다는 특징이 있다.
print (Family.lastname) # 클래스이름.클래스변수로 사용
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
#클래스의 lastname을 변경하면 어떯게 될까?
Family.lastname = "박"
print(a.lastname)
print(b.lastname) # 클래스로 만든 객체의 lastname값도 변경이 된다는 것을 확인할 수 있다. 
print()

## 클래스 변수와 객체 변수 
# 객체 변수 변경 
a.lastname = "최" 
print(a.lastname)
# 객체변수를 변경도 클래스 변수는 상관이 없다. 
print(Family.lastname)
print(b.lastname)