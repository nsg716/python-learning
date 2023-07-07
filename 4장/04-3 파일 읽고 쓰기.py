#  파일 생성하기 
"""
f = open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/새 파일.txt",'w')
f.close() # 실슬을 위해 주석 처리 새파일 생성을 할려면 주석을 없애면 된다.
"""
# 파일을 생성하기 위해 파이썬 내장 함수 open을 사용하였다. 4장 디렉토리에 새파일 생성
"""
open 함수
파일 객체 = open(파일 이름,파일 열기 모드)

""" 


# 파일 열기 모드 종류 
"""
r - 읽기 모드 : 파일을 읽기만 할 때 사용 
w - 쓰기 모드 : 파일에 내용을 쓸 때 사용
a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용   

"""

"""
실습 1 : writedata.py
"""

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법 
# 1. readline 함수 사용 
"""
실습 2 : readline.py
실습 3 : readline_ all.py1
"""
# 사용자의 입력을 받아서 출력하는 것 (위의 실습과 비슷)
"""
while 1:
    data = input()
    if not data:
        break
    print(data)

    """ #실습을 위해서 주석 처리 
# 2. readlines함수 사용하기 
f = open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/새 파일.txt",'r')
lines = f.readlines() 
for line in lines:
    print(line)
f.close()
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
# 3. read 함수 사용하기 
f = open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/새 파일.txt",'r')
data = f.read()
print(data)
f.close()
# f.read()는 파일의 내용 전체를 문자열로 돌려준다. 

#파일에 새로운 내용 추가하기 - 파일을 추가모드 'a' 로 열면 된다. 
"""
실습 4. adddata.py
"""
# with 문과 함께 사용하기 
# 파일을 열고 닫을 때, f.open, f.close 를 사용하였다. 이를 자동으로 처리해주는 것이 with 문이다. 
with open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/foo.txt","w") as f:
    f.write("Life is too short, you need python")
# 파일이 전부다 실행된다. 

## 파이썬에서 sys 모듈로 매개변수 주기 
"""
실습 5.sys1.py
실습 6.sys2.py
"""