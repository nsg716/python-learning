# 숫자형 자료형 파이썬으로 다루기

a = 1 + 2j
print(a.real)  # 복소수의 실수 부분 리턴

b = 3 + 4j
print(b.imag)  # 복소수의 허수 부분 리턴

c = 5 + 6j
print(c.conjugate())  # 복소수의 켤레 복소수값을 리턴

# 숫자형을 활용하기 위한 연산자 (사칙연산)
a1 = 3
b1 = 4
print(a1 + b1)  # 덧셈 연산자
print(a1 - b1)  # 뺄셈 연산자
print(a1 * b1)  # 곱셈 연산자
print(a1 / b1)  # 나눗셈 연산자
print(a1 % b1)  # 나머지 연산자
print(a1 // b1)  # 나눗셈후 소숫점 아랫자리를 버리는 연산자
