# 문자형 자료형 파이썬으로 다루기

# 문자열을 만드는 방법은 총 4가지

# 1.큰 따음표로 둘러싸기
print("안녕하세요.")
# 2. 작은 따음표로 둘러싸기
print('반갑습니다.')
# 3. 큰 다음표 연속 3개를 사용하여 둘러싸기
print("""지금은 파이썬을 사용하고 있습니다.""")
# 4. 작은 따음표를 연속 3개 사용하여 둘러싸기
print('''문자형 자료형을 다루고 있습니다.''')

# 문자열 안에 작은 따음표나 큰 따음표 포함시키기
# 1. 큰 따음표로 작은 따음표 감싸기
print("you're so happy!")
# 2. 작은 따음표로 큰 따음표 감싸기
print('you"re so happy!')
# 3. \를 이용하여 따음표 표현하기
print("\"you\'re so happy!\"")

# 여러 줄인 문자열을 표현하고자 할 때

# 1. 줄을 바꾸기 위한 이스케이프 코드 '\n' 삽입
multiline1 = "phrase1.11111\n22222"
# 2. 연속된 따음표 사용
multiline2 = """
phrase2.11111
22222
"""
multiline3 = '''
phrase3.11111
22222
'''
print(multiline1)
print(multiline2)
print(multiline3)

# 문자열 더하기
head = "안녕하세요"
tail = "반갑습니다"
print(head + tail)

# 문자열 곱하기
print(head * 2)

# 문자열 연산 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱(가리키는 것), 슬라이싱(잘라내는 것)
test_a = "0123456789"

# 문자열 인덱싱
print(test_a[0])
print(test_a[1])
print(test_a[-1])  # 뒤에서부터 시작한다.

# 문자열 슬라이싱
print(test_a[0] + test_a[2] + test_a[3])
print(test_a[0:4])  # [시작번호:끝번호] [0:4] -> 수식은 0<= test_a < 4이다.즉 test_a[0] 부터 test_a[3] 까지 출력한다.
print(test_a[0:])  # 생략하면 생략한 부분까지 전부 다 출력한다.
print(test_a[:9])
print(test_a[:])
print(test_a[1:-1])  # - 기호 사용 가능

# 문자열 슬라이싱 응용
dataw = "20210802Rainy"
print(dataw[:4])  # year
print(dataw[4:8])  # date
print(dataw[8:])  # weather

# 문자열 포매팅
# 1. 숫자 바로 대입
print("%d" % 3)
# 2. 문자열 바로 대입
print("%s" % "four")
# 3. 숫자값을 나타내는 변수로 대입
number = 2
print("%d" % number)
# 4. 2개 이상의 값을 넣기
print("%s %d" % (test_a, number))

# 포맷 코드와 숫자 같이 사용하기

# 1. 정렬과 공백
print("%10sSDW" % "hi")
print("%-10sSDW" % "hi")

# 2. 소수점 표현하기
print("%0.4f" % 3.123356789)  # 표현하지 못한 소수점밑자리는 올림으로 표시한다.
print("%10.4f" % 3.123356789)  # 표현하지 못한 소수점밑자리는 올림으로 표시한다.

# 문자열 관련 함수들

# 문자 개수 세기 (count)
print(test_a.count("0"))

# 위치 알려주기 1(find)
print(test_a.find("1"))
print(test_a.find("10"))  # 문자열중에 일치한 값이 없으면 -1을 반환한다.
# 위치 알려주기 2(index)
print(test_a.index("3"))  # 문자열 중에 일치한 값이 없으면 오류 발생

# 뮨자열 삽입 (join)
comma = ","
print(comma.join("12345"))

# 소문자를 대문자로 바꾸기 (upper)
small = "small"
print(small.upper())
# 대문자를 소문자로 바꾸기 (lower)
BIG = "BIG"
print(BIG.lower())

# 공백 지우기 ((l,r)strip)
a2 = "    123     "
print(a2.lstrip())  # 왼쪽 공백 지우기
print(a2.rstrip())  # 오른쪽 공백 지우기
print(a2.strip())  # 양쪽 공백 지우기

# 문자열 바꾸기 (replace)
a3 = "Life is too long"
print(a3.replace("Life", "You arm"))

# 문자열 나누기  (split)
print(a3.split())  # 공백을 기준으로 나눈다.
a4 = "Life:is:too:long"
print(a4.split(':'))  # : 기호를 기준으로 문자열을 나눔

# 고급 문자열 포매팅 (format)

# 숫자 대입하기
a5 = "{0}".format(3)
print(a5)  # {0} 이 숫자 3으로 바뀌었다.
# 문자열 대입하기
a5 = "{0}".format("five")
print(a5)  # {0} 이 문자열 five 으로 바뀌었다.
# 숫자 값을 가진 변수로 대입하기
a5 = "{0}".format(test_a)
print(a5)  # {0} 이 변수의 값으로 변하였다.
# 이름으로 넣기
a5 = "{day}".format(day=3)
print(a5)

# 왼쪽 정렬
a5 = "{0:<10}".format("hi")
print(a5)
# 오른쪽 정렬
a5 = "{0:>10}".format("hi")
print(a5)  # 화살표 방향에서 어느 방향에 정렬이 되는지 알 수 있다.
# 가운데 정렬
a5 = "{0:^10}".format("hi")
print(a5)

# 공백 채우기 (<,>,^ 앞에 사용을 해야 한다.)
a5 = '{0:=^10}'.format("hi")  # 오류가 발생을 하지만 정상적으로 작동을 하게 된다. 
print(a5)
