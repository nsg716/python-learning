#sys1.py
import sys
# 파이썬은 sys 모듈을 사용하려면  import 명령어를 사용해야 한다. sys 모듈은 매개변숭에 직접 줄수 있다.
"""
명령 프롬프트 명령어 [인수1, 인수2 ...]

"""
# 입력받는 인수를 for 문을 사용하여 차례대로 하나씨 출력하는 예이다. sys 모듈의 argv는 명령창에서 입력한 인수를 의미한다.
args = sys.argv[1:]
for i in args:
    print (i) 
# 터미널에 4장으로 이동하고 Python [파일명] aaa bbb ccc 를 입력하면 다음과 같이 나온다.
"""
aaa
bbb
ccc 
"""