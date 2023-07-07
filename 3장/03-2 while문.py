# while문 
# 반복해서 문장을 수행해야 할 경우 while 문을 사용한다. 
# while문은 반복문이라고 부른다. 

# while문의 기본 구조 
"""
while 조건문 : 
    수행할 문장:
    수행할 문장:
    수행할 문장:
    ...

"""
# while 문장의 조건문이 참인 동안 while 아래의 문장이 반복해서 실행한다. 

# 예시 : 열 번 찍어서 안넘어가는 나무는 없다. 
treeHit = 0 # 나무를 찍은 횟수
while treeHit < 10 : # 나무를 찍은 횟수가 10보다 작은 동안 반복
    treeHit = treeHit + 1 # 나무 찍은 횟수 1 씩 증가

    print ("나무를 %d 번 찍었습니다." %treeHit )
if treeHit == 10 : # 나무 열 번 찍으면 
    print ("나무가 넘어갑니다.")
print()

# while문 만들기 
# 여러가지 선택지 중에서 하나를 선택해서 입력 받는 예제 
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number """
# 예제 1 : 특정 번호를 입력하지 않으면 계속 실행되는 반복문 (다음 실습을 위해서 number 4로 설정 / 아래 예제 실습시 number은 0으로 설정) 
number = 4 # 번호를 입력받는 변수 
while number != 4 : # 4 를 입력하지 않으면 prompt 출력
    print(prompt)
    number = int(input()) # 내장 함수부분에서 자세히 다룬다

print ()
# 1,2,3을 터미널에 입력하면 계속 반복이 되지만 4를 입력하면 조건문이 거짓이 되면서 빠져나온다.

# while 문 강제로 빠져나가기 

# while 문에서 조건문이 참인 경우에도 멈추는 것이 바로 break 문이다. 

# 예제 2 : break 문 활용 - 커피 자판기 
coffee = 10  # 커피의 총량 
money = 300 # 자판기에 넣은 돈은 300원 고정이다.
while money : 
    print ("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1 
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print ("커피가 다 떨어졌습니다. 판매를 중지합니다. ")
        break
print ()
# coffee의 갯수가 0일 때 break 문이 호출되어 while 문을 빠져나간다.
"""

실습 1.coffee.py  


"""


# while문 맨 처음으로 돌아가기 
# while 문을 빠져나가지 않고, 조건문으로 되돌아가는 경우가 생긴다. - continue문

# 홀수만 출력하는 while 문
a = 0
while a < 10 : 
    a = a + 1 # a는 1부터 시작 
    if a % 2 == 0 : # a가 짝수이면 실행 
        continue # a를 2로 나누었을 때 나머지가 0 이면 맨 처음으로 돌아간다. 
    print(a)  
print ()
# 무한 루프 - 무한히 반복을 한다는 의미이다. / 자주 사용한다. 

while True : 
    print ("Ctrl + C를 눌러야 while 문을 빠져나갈 수 있습니다.")
