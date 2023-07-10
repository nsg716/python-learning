# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들자 
"""
필요한 기능은 ? 메모 추가하기 
입력받는 값은 ? 메모내용, 프로그램 실행 옵션 
출력하는 값은 ? memo.txt

"""
# 가장 먼저 해야할 일은 메모를 추가 하는 것이다. 
# 받은 옵션과 메모를 출력하는 코드를 작성 
"""
실습 1. D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)/6장 memo.py

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장>python memo.py -a "Life is too short"
-a
Life is too short

입력으로 전달한 옵션과 메모 내용이 그래도 출력되는 것을 확인할 수 있다. 

"""

# 입력으로 받은 메모를 파일에 작성하도록 코드를 변경해보자 
"""
실습 2. D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)/6장 memo.py

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장>python memo.py -a "Life is too short"
-a
Life is too short

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장>python memo.py -a "You need Python"   
-a
You need Python

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장>type memo.txt
Life is too short
You need Python

"""

# 작성한 메모를 출력하는 부분을 만들 것이다.
"""
실습 3. D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)/6장 memo.py

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장>python memo.py -v
Life is too short
You need Python
"""
