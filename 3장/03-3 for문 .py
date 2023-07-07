# 파이썬의 직관적인 특징을 잘 표현해주는 것이 바로 이 for 문이다. 

# for 기본구조 
"""
for 변수 in 리스트 (또는 튜플, 문자열)
    수행할 문장 1
    수행할 문장 2 
...

"""
#전형적인 for 문
test_list = ['one','two','three']
for i in test_list : # one, two,three 차례대로 대입한다. 
    print (i)
print ()

# 다양한 for 문 사용 
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print (first + last)
print()
# 3
# 7 
# 11 
# 위 예는 a 리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입한다. 
"""

 실습 : 총 5명의 학생이 시험을 보았는데 시험점수가 60점이 넘으면 합격이고, 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오.
 실습 1.marks1.py
 실습 2.marks2.py

 """

# for문과 함께 자주 사용되는 range 함수 
# for 문은 숫자 리스트를 자동으로 만들어주는 range 함수와 함께 사용 하는 경우가 많다. 

# range 함수의 사용법 
a1 = range(0,10)
print (a1) # 0부터 10미만의 숫자를 포함하는 객체를 만들어 준다 .(0,1,2,3,4,5,6,7,8,9)
a2 = range(1,11)
print (a2) # (1,2,3,4,5,6,7,8,9,10)

# range 함수의 사용법 
add = 0
for i in range(1,11) :
    add = add + i
print (add) # 1무터 10까지 더한 수 
print ()
"""
실습 3.marks3.py  
""" 
# for range를 사용한 구구단 
for i in range (1,10) :
    for j in range(1,10) :
        print (i*j, end = " ")
    print()       # 1단,2단 . 단을 나누는 부분  
print ()
# 매개변수 end = " " 를 넣어둔 이유 : 해당 결과값에서 다음줄로 넘기지 않고, 그 줄에 계속해서 출력하기 위해서이다.


# 리스트 내포 사용하기 (List comprehension) - 좀 더 편리하고 직관적인 프로그램을 만들 수 있다. 

a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)

print (result)

# 위 예제는 a 리스트의 각 항목에 3을 곱한 결과를 result에 예제 이다. 

# 리스트 내포 사용 
a = [1,2,3,4]
result = [num * 3 for num in a]
print  (result)

# 리스트 내포 사용 짝수에만 3을 곱하여 담고 싶다면 다음과 같이 if 조건을 만들 수 있다. 
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print  (result)
print()
""""
  리스트 내포의 일반 문법은 다음과 같다. 
   - [표현식 for 항목 in 반복 가능 객체 if 조건] 
 for문을 2개 이상 사용하는 것도 가능하다. 
    [표현식 for 항목1 in 반복 가능 객체1 if 조건1] 
            for 항목1 in 반복 가능 객체2 if 조건2]
            ...
            for 항목n in 반복 가능 객체n if 조건n]
 """
 # 구구단 리스트 내포
result1 = [x * y for x in range(2,10)
    for y in range(1,10)]
print(result1)