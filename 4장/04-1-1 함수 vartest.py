# vartest.py
a = 1 # 함수 밖의 변수  
def vartest (a):
    a = a +1  
vartest(a)  #vartest 함수의 입력값으로 a를 줌
print(a)    # a 값 출력 

# 함수 안에서 사용되는 매개변수는 전혀 영향이 없다. 

