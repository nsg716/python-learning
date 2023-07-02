# 리스트 자료형 파이썬으로 배우기

# 리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])

# 다중 리스트
a1 = [1, 2, 3, ['a', 'b', 'c']]
print(a1[0])
print(a1[3])
# 다중 리스트에서의 표현
print(a1[3][0])  # 첫 번째 요소를 불러오기 위해서 다음과 같이 표현한다.
# 마치 C나 JAVA 처럼 배열을 사용한다.

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])  # 문자열 슬라이싱과 동일하다
b = a[:2]
c = a[2:]
print(b)
print(c)

# 리스트 연산자
print(b + c)
print(a * 2)

# 리스트 값 수정, 변경, 삭제
# 수정
a[3] = ["a", 'b', "c"]
print(a)
a[1:2] = ["A", "B", "C"]
print(a)

# []를 이용하여 리스트 요소 삭제하기
a[1:3] = []
print(a)

# del 함수를 사용하여 리스트 요소 삭제하기
del a[1]
print(a)

# 리스트 관련 함수들

# 리스트에 요소 추가 (append)
a = [1, 2, 3, 4, 5]
a.append(6)  # 리스트 마지막 요소에 추가
print(a)
a.append([5, 6])
print(a)

# 리스트 정렬 (sort)
a1 = [1, 4, 5, 6, 2, 3, 12, 10, 9]
a1.sort()  # 순서대로 정렬 알파벳도 순서대로 정렬한다.
print(a1)

# 리스트 뒤집기 (reverse)
a.reverse()  # 현재의 리스트를 거꾸로 뒤집을 뿐이다.
print(a)

# 위치 변환 (index)
print(a.index(3))  # 3은 a[2]에 있으므로 4가 나온다.
print(a.index(1))  # 1은 a[0]에 있으므로 6이 나온다.
# index(x) 함수는 리스트에 x 라는 값이 있으면 x의 위치값을 리턴시킨다.

# 리스트에 요소 삽입 (insert)
a = [1, 2, 3, 4, 5]
a.insert(0, 4)  # a[0] 자리에 4가 들어간다.
print(a)

# 리스트 요소 제거 (remove)
a.remove(4)
print(a)  # remove(x)는 첫 번째로 나오는 x를 지우는 함수이다.

# 리스트 요소 끌어내기 (pop)
a = [1, 2, 3, 4, 5]
print(a.pop())  # pop()는 리스트의 맨 마지막 요소를 톨려주고 그 요소는 삭제한다.
a = [1, 2, 3, 4, 5]
print(a.pop(0))  # pop(x)는 리스트의 x 번째 요소를 돌려주고 그 요소를 삭제한다.
print(a)

# 리스트에 포함된 요소 x의 개수 세기 (count)
a = [1, 2, 3, 4, 5]
a.count(1)  # 1이라는 값이 1개 있으므로 1개의 값을 리턴한다.
print(a)

# 리스트 확장 (extend)
print(a)
a.extend([6, 7])  # extend(x)에서 x에는 리스트만 올 수 있으며 a 리스트에 x를 더하게 된다.
print(b)
a.extend(b)
print(a)
a.extend([["a", "b"]])
print(a)
