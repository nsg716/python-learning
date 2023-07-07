# vartest_error.py
"""def vartest (a):
    a = a +1  
vartest(3)  
print(a) """  
# 오류 발생 : 이유는 a 변수를 어디에서 찾을 수 없기 때문이다.
# 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서 사용되지 않는다.