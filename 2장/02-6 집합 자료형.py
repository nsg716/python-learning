# 집합 자료형은 set 키워드를 사용하여 만들 수 있다.
# 예시 
s = set() # 비어있는 집합 자료형 
s1 = set ([1,2,3])
print (s1)
s2 = set ("Hello") # 순서가 뒤죽박죽인 것은 집합 자료형의 특징이다. 
print (s2) 

# 집합 자료형의 특징 
 # - 중복을 허용하지 않는다. 
 # - 순서가 없다. (Unordered) 


# set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환하여야 한다. 
s1 = set ([1,2,3])
l1 = list(s1) # 리스토로 변환 
print (l1)
print (l1[0])
t1 = tuple(s1) # 튜플로 변환
print (t1)
print (t1[0])
print ()


# 교집합,합집합, 차집합 구하기 
s1 = set({1,2,3,4,5,6})
s2 = set({4,5,6,7,8,9})

# 교집합 
print (s1 & s2) # & 기호를 사용하면 교집합을 간단히 구할 수 있다.
print (s1.intersection(s2)) # 교집합 함수이다. s2.intersection(s1)도 마찬가지이다.
 
# 합집합
print (s1 | s2) # | 기호 사용 
print (s1.union(s2)) # 합집합 함수이다. s2.union(s1) 도 마찬가지이다.

# 차집합
print (s1 - s2) 
print (s2 - s1) # - 기호를 사용한 방법이다.
print (s1.difference(s2))
print (s2.difference(s1)) # difference 함수로 차집합을 구할 수 있다. 
print ()


# 집합 자료형 관련 함수 
# 값 1개 추가하기 (add)
s1 = set ([1,2,3])
s1.add(4)
print (s1)

# 값 여러개 추가하기 (update) - 한꺼번에 추가할 때
s1 = set ([1,2,3])
s1.update([4,5,6])
print (s1)

# 특정 값 제외하기 (remove)
s1 = set ([1,2,3])
s1.remove(2)
print (s1)