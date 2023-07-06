# 불(bool) 자료형은 참(True)과 거짓(False)을 나타내는 자료형이다.  True, False 는 예약어이기 때문에 첫 문자는 항상 대문자이다.
a = True
b = False

# 변수의 자료형 확인 
print(type(a))
print(type(b)) # 둘다 bool 자료형이다.
print (1==1) # 조건문의 반환값으로 사용이 가능하다.
# 조건문의 결과로  True, False 를 돌려준다.
print (2>1)
print (2<1)
print ()

#자료형의 참과 거짓
# 문자열, 리스트 ,튜플, 딕셔러니 등 값이 비어있으면 False를 돌려준다.비어있지 않으면 True 를 돌려받는다.
# 숫자형에서는 그 값이 0이면 False를 박는다. 

# 불연산 
print (bool('python')) # 비어있지 않으므로 참
print (bool('')) # 비어있으므로 거짓
# 예제 추가 
print (bool([1,2,3])) # 참
print (bool([])) # 거짓
print (bool(0)) # 거짓
print (bool(3)) # 참

# 여기까지가 파이썬의 근간이다. 약 50% 정도 라고 하니 복습 잘 하기 