# 문자열을 만드는 방법 

# 1. 큰따음표 ("") 로 양쪽 둘러싸기 
print("Hello world!")

# 2. 작은 따음표 ('') 로 양쪽 둘러싸기
print ('Python is fun')

# 3. 큰 따음표 3개를 연속("""""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""") 

# 4. 작은 따음표 3개를 연속('''''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''') 
print()

#문자열에 작은 따음표나 큰 따음표를 포함시키고 싶을 떄
#문자열에 작은 따음표를 포함시키려면 큰 따음표로 둘러 싸야하고 큰 따음표를 포함시키려면 작은 따음표로 둘러 싸면 된다. 
# 1. 문자열에 작음 따음표 포함시키기
food = "Python's favorite food is perl"
print (food)

# 2. 문자열에 큰 따음표 포함시키기
say = '"Python is very easy." he says'
print (say)

# 3. 백슬래시를 사용해서 작은 따음표와 큰 따음표를 포함시키기
food1 = 'Python\'s favorite food is perl'
say1 = "\"Python is very easy.\" he says"
print (food1)
print (say1)
print()


#여러 줄인 문자열을 변수에 대입하고 싶을 때 
# 1. 줄을 바꾸는 이스케이프 코드 '\n' 삽입하기
multiline1 = "Life is too short\nYou need python"
print (multiline1)
# 2. 연속된 작은 따음표 3개 (''') 혹은 큰 따음표 3개 ("""") 사용하기  
multiline2 = '''
Life is too short
You need python
'''
multiline3 =  """
Life is too short
You need python
"""

print (multiline2,multiline3)
print ()

# 문자열 연산하기 
# 1. 문자열 더해서 연결하기 (Concatenation)
head = "Python"
tail = " is fun!"
print (head + tail)

# 2. 문자열 곱하기 
print (head * 2)

# 3. 문자열 곱하기 응용 
print ("=" * 50)
print ("My Program")
print ("=" * 50)

# 4. 문자열 길이 구하기 
length = "Life is too short"
print(len(length))
print()

# 문자열 인덱싱과 슬라이싱 
# 인덱싱 = 가리킨다. 슬라이싱  = 잘라낸다. 
# 인덱싱
Life = "Life is too short, You need Python" 
print(Life[3]) # 문자열에 번호를 매기면 'e' 가 나온다. 문자열이기 때문에 시작은 0부터

# 인덱싱 활용하기 
print (Life[0],Life[12],Life[-1],Life[-2],Life[-5]) # Lsnoy 가 나오면 된다. 음수는 뒤에서 부터 

# 문자열 슬라이싱 
b1 = Life[0] + Life[1] + Life[2] + Life[3] # = Life[0:4]
# 슬라이싱 범위 
# Life[x] 0 =< x < 4
print (b1, Life[0:4])

# 문자열 슬라이싱 방법
print(Life[0:5])
print(Life[0:2])
print(Life[5:7])
print(Life[12:17])
# [시작번호 : 끝번호] 부분을 생략하면 시작번호부터 그 문자열의 끝까지 뽑아 낸다. 
print(Life[19:])
print(Life[:17])
print(Life[:])
print(Life[19:-7])

# 슬라이싱으로 문자열 나누기 
today = "20010331Rainy"
date = today[:8]
weather = today[8:]
print (date,weather)
year = today[:4]
day = today[4:8]
print (year,day,weather)
print ()

# 문자열 포매팅 - 문자열 안에 어떤 값을 삽입하는 방법  
# 1. 숫자 바로 대입 
print ("I eat %d apples" %3)
# 2. 문자열 바로 대입
print ("I eat %s apples" %"five")
# 3. 숫자 값을 나타내는 변수로 대입
num1 = 3 
print ("I eat %d apples" % num1) 
# 4. 2개 이상의 값 넣기 - 값을 , 로 구분하기 
num2 = 10
day2 = "three"
print ("I ate %d apples, so I was sick for %s days." %(num2,day2))

# %s 코드 및 %% 코드 추가 설명 
# %s 어떤 형태의 값이든 변환해 넣을 수 있다. 
print ("I have %s apples" % 3) 
print ("rate is %s" % 3.234)
# 문자 % 를 사용 하기 위해 %%을 사용한다.
print ("Error is %d%%." % 98)
print()
# 포맷 코드와 숫자 함께 표현하기 
# 정렬과 공백 
# 오른쪽 정렬
print ("%10s" % "hi")
# 왼쪽 정렬
print ("%-10sJane" % "hi")
# 소수점 표현하기 
print("%0.4f" % 3.42134234) # 소수점 네자리까지 표시
print("%10.4f" % 3.42134234) # 소수점 네자리 표시 및 전체 길이가 10
print()

# format 함수를 사용한 포매팅 
# - format 함수를 사용하면 문자열 포맷을 지정할 수 있다. 
# 숫자 바로 대입하기 
print ("I eat {0} apples".format(3))
# 문자열 바로 대입하기
print ("I eat {0} apples" .format("five"))
# 숫자 값을 가진 변수로 대입하기
num3 = 3 
print ("I eat {0} apples" .format(num3))
# 2개 이상의 값 넣기  
num4 = 10
day5 = "three"
print ("I ate {0} apples, so I was sick for {1} days." .format(num4,day5))
# 이름으로 넣기 - {name}형태를 사용하면 format 함수에는 반드시 name = value  와 같은 형태의 입력 값이 있어야 한다.
print ("I ate {number} apples, so I was sick for {day} days." .format(number=10,day=3))
# 왼쪽 정렬
print("{0:<10}".format("hi"))
# 오른쪽 정렬 - 부등호 표시 방향으로 정렬 방향을 알 수 있다.
print("{0:>10}".format("hi")) 
# 가운데 정렬 
print("{0:^10}".format("hi"))
#공백 채우기 - 채워 넣을 문자 값은 정렬 문자 바로 앞에 넣어야 한다.
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
# 소수점 표현하기 
float = 3.41234234
print("{0:0.4f}".format(float))
print("{0:10.4f}".format(float))
# {또는} 문자 표현하기
print("{{and}}".format())
print()


# f 문자열 포매팅 - 파이썬 3.6 이상 부터 사용 가능 / 변수값을 생성한 후에 그 값을 참조할 수 있다. 
name1 = '홍길동'
age = 20 
print(f'나의 이름은 {name1}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 됩니다.')
# 딕셔너리 f 문자열 포매팅
d = {'name' : '홍길동', 'age' :'30'}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
# 정렬
print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬
# 공백 채우기 
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')
# 소수점 표현 
print(f'{float:0.4f}')
print(f'{float:10.4f}')
#{}문자 표현 
print(f'{{and}}')
print()

#문자열 관련 함수
# 문자 세기 함수 - count
a1 = "hobby"
print(a1.count('b')) # 문자 b 의 개수를 돌려준다. 

# 위치 알려주기 1 (find)
a2 = "Python is the best choice"
print(a2.find('b')) # 문자열의 위치 : 14
print(a2.find('k')) # 문자열에 해당 문자가 없을 경우 -1 반환
# 위치 알려주기 2 (index)
a3 = "Life is too start"
print(a3.index('t')) # 문자열에서 해당 t 의 위치를 알려줌
## print(a3.index('k')) - 오류 발생 : 존재하지 않기 때문에

# 문자열 삽입 (join)
print(",".join('abcd')) # 각의 문자 사이에 "," 를 삽입한다. 리스트나 튜플에소 사용 가능 

# 소문자를 대문자로 바꾸기 (upper)
a4 = "hi"
print(a4.upper())

# 대문자를 소문자로 바꾸기 (lower)
a5 = "HI"
print(a5.lower())

# 왼쪽 공백 지우기 (lstrip)
a6 = "hi    "
print(a6.lstrip()) # 한 칸 이상의 연속된 공백들을 모두 지운다.

# 오른쪽 공백 지우기 (rstrip)
a7 = "    hi"
print(a7.rstrip()) # 한 칸 이상의 연속된 공백들을 모두 지운다.

# 양쪽 공백 지우기 (strip)
a8 = "    hi    "
print(a8.strip()) # 한 칸 이상의 연속된 공백들을 모두 지운다.

# 문자열 바꾸기 (replace)
a3 = "Life is too start"
print(a3.replace("Life", "Your leg")) # replace ("바뀌게 될 문자열", "바꿀 문자열")

# 문자열 나누기 (split)
print(a3.split()) # 공백을 기준으로 문자열 나눔
b = "a:b:c:d"
print(b.split(':')) # 기호를 기주능로 문자열 나눔

 
