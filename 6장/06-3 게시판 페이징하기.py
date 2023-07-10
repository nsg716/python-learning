# 게시판의 페이지 수를 보여주는 것을 '페이징'이라고 한다.
# 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때, 총 페이지 수를 출력하는 프로그램이 필요하다
"""
함수 이름은 getTatalPage
입력받는 값은 : 게시물의 총 건수(m), 한 페이지에 보여줄 건수(n)
출력하는 값은 : 총 페이지 수

"""
"""
게시물의 총 건수 (m)    페이지 당 보여줄 건수 (n)   총 페이지 수 
        5                         10                  1
        15                        10                  2
        25                        10                  3
        30                        10                  3

"""
# 이 문제는 게시판 프로그램을 만들 때, 가장 처음 마주치는 난관이라고 할 수 있는 총 페이지수를 구하는 문제이다. 
# 사실 실제 업무에서 사용하는 페이징 기술은 훨씬 더 복잡하다.
# 가장 간단한 총 페이지 수를 구한는 방법에 대해 알아본다.

# 총 페이지수에 관한 공식 
# 총 페이지수 = (총 건수 / 한 페이지 당 보여 줄 건수 ) + 1
# 공식과 관련된 함수 제작
def getTotalPage(m,n):
    return m // n + 1 
print (getTotalPage(5,10))  # 첫 번째 케이스 , 1이 출력됨
print (getTotalPage(15,10)) # 두 번째 케이스 , 2가 출력됨
print (getTotalPage(25,10)) # 세 번째 케이스 , 3이 출력됨
print (getTotalPage(30,10)) # 네 번째 케이스 , 4가 출력됨 -> 실패 
print ()

# 수정 

def getTotalPage(m,n):
    if m % n == 0: # 나머지가 0인경우 나누기의 몫만 돌려주고 그 이외의 경우에는 1을 더하여 돌려준다. 
        return m //n
    else : 
        return m // n + 1 
print (getTotalPage(5,10))  
print (getTotalPage(15,10)) 
print (getTotalPage(25,10))
print (getTotalPage(30,10))