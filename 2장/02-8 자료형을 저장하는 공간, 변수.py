# 변수 이름 = 변수에 저장할 값 
# 변수란 객체를 가리키는 말이다.  (객체는 5-1에서 제대로 공부)
a = [1,2,3]
print (a) 
# a = [1,2,3]이라는 리스트 자료형(객체)이 자동으로 메모리에 생성되고 변수 a는 [1,2,3] 리스트가 저장된 메모리의 주소를 가리키게 된다.
print()

# 변수가 가리키는 메모리의 주소
print(id(a)) 
# 변수 a 가 가리키는 주소값은 31000260990528임을 알 수 있다. / 값은 계속 변동된다.
print()

# 리스트를 복사할 때
a = [1,2,3]
b = a
print (id(a),id(b)) # a 가 가라키는 대상과 b가 가리키는 대상이 동일하다는 것
print( a is b) # True
# a리스트를 변경하면 b 리스트도 바뀔까?
a[1] = 4
print (a,b) 
print( a is b) # True
# b 도 바뀌는 이유는 동일한 리스트이기 때문이다.
print ()

# b 변수를 생성할 때, a 변수의 값을 가져오면서 a 와는 다른 주소를 가리키도록 만드는 방법
# 1. [:] 사용 - 리스트 전제 복사 
a = [1,2,3]
b = a [:] # 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱 
a[1] = 4
print (a,b) 
print (b is a) # False
print ()
# 2.copy 모듈 사용 
from copy import copy # 파이썬 모듈에서 자세히 설명, copy 함수를 쓰기 위해서 사용하는 것 
a = [1,2,3]
b = copy(a)
a[1] = 4
print (a,b)
print (b is a) # False # b 와 a 의 객체는 서로 다르다는 것을 알 수 있다.
print ()

# 변수를 만드는 방법 
a1, b1 = ('python', 'Life') #  튜플
print (a1,b1) 
(a1 ,b1) = 'python', 'Life' # 괄호는 생략 가능
print (a1,b1)
[a1,b1] = ['python', 'Life'] # 리스트
print (a1,b1) 
a1 = b1 = 'python' # 변수에 같은 값 대입 
print (a1,b1)
# 변수 교환 
a = 3
b = 5 
a, b = b, a
print (a,b) # 5,3