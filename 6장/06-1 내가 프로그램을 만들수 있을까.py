# 프로그램을 만들려고 하면 먼저 다른 사람이 만든 프로그램을 자세히 들여다 보고 분석하는데서 시작하는 것이 좋다. 
# 가장 중요한 것은 자신의 수준에 맞는 소스를 찾는 일이다. 
# 프로그램을 만들려면 가장 먼저 "입력" 과 "출력" 을 생각해라 

# 구구단 2단 만들기 
"""
함수 이름 : GuGu
입력값 : 2
출력값 : 2,4,6,8,...,18
결과 : 연속된 자료형이므로 리스트 

"""
# 함수를 만드는 생각 순서 
"""
# 1. 함수에 입력값을 넣고 result에 결괏값을 넣는다.
# 2. 함수를 만들고 입력값을 넣어 출력값이 나오게 작동하기
# 3. 결괏값을 담을 리스트 생성 
# 4. 리스트에 요소를 추가하는 내장 함수 제작
# 5. 반복문을 이용하여 간략화 

"""
# 완성된 예시
def GuGu(n) :
    result = [] # 결괏값을 저장할 리스트 result
    i = 1 
    while i < 10 :
        result.append(n*i)
        i = i + 1
    return result
# 테스트 
print (GuGu(2))