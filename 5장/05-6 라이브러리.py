# 전 세계의 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓는 것이 파이썬 라이브러리이다. 

# sys
# sys 모듈을 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다. 

# 명령행에서 인수 전달하기  - ays.argv
"""
실습 1 : Mymod - argv_test.py

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\5장\Mymod>python argv_test.py you need python
['argv_test.py', 'you', 'need', 'python']

"""
# 강제로 스크립트 종료하기 - sys.exit / 같은 기능 - 컨트롤 z, 컨트롤 d

# 자신이 만든 모듈 불러와 사용하기 - sys.path 
import sys 
sys.path
"""
실습 2. path_append.py
"""

# pickle - 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법
import pickle
f = open("D:\코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/5장/test.txt",'wb')
data = {1 : "python" , 2 : 'you need'}
pickle.dump(data,f)
f.close
print ()
# pickle.dump 로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체 (data) 상태 그대로 불러오는 예
import pickle
f = open("D:\코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/5장/test.txt",'rb')
data = pickle.load(f)
print (data)
# 딕셔너리 객체를 사용했지만 어떤 자료형이든 저장하고 불러올 수 있다. 
print ()

# OS
# OS 모듈은 환경변수나 디렉터리, 파일등의 OS 자원을 제어할 수 있게 해주는 모듈
# 내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ : 현재 환경 변수값을 보여준다. 

import os
print(os.environ)
print ()
print(os.environ['PATH'])
print ()

# 현재 디렉토리 위치 변경 - os.chdir
# os.chdir("변경할 디렉토리 위치")
# 디렉토리 현재위치 돌려받기 - os.getcwd
print (os.getcwd()) 
print ()

# 시스템 명령어 호출하기 - os.system
# 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수 있다. 
print (os.system("dir")) # 시스템 명령어 "dir" 을 실핼하는 예

# 실행한 시스템의 명령어의 결괏값 돌려받기 - os.popen
f = os.popen("dir") # 0 읽기 모드 형태의 파일 객체로 돌려준다. 
# 읽은 파일 객체의 내용을 보기 위한 방법 
print(f.read())
print ()
##기타 유용한 os 함수 
"""
os.mkdir(디렉터리)  디렉터리 생성
os.rmdir(디렉터리)  디렉터리 삭제 (디렉터리가 비어있어야 한다.)
os.unlink(파일 이름)파일을 지운다.
os.rename(src.dst)  src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""

#shutil - 파일을 복사해주는 파이썬 모듈이다. 
# src 파일을 dst 로 복사한다. 만약 dst가 디렉터리 이름이면 src라는 파일이름으로 dst 디렉토리에 복사하고, 동일한 파일은 덮어쓴다.
""" 실습을 위하여 주석 처리 - 파일이 있어야 실습 가능
import shutil
shutil.copy("src.txt","dst.txt")
"""

# glob - 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두 알아야 할 때 사용 
# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
# mark로 시작하는 파일을 모두 찾아서 읽어들이는 예
import glob
print (glob.glob("D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)/mark*"))
# 03-3-1 이 있어서 터미널에 안보이지만 작동은 할 수 있다. 
print ()

# tempfile - 파일을 임시로 만들어서 사용할 때 유용한 모듈 
# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
import tempfile
filename = tempfile.mkstemp()
print (filename)
#tempfile.TempraryFile() 은 밈시 저장공간으로 사용할 파일 객체를 돌려준다. 이 파일은 기본적으로 바이너리 쓰기 모드 (wb)를 갖는다.
#f.close 가 호출되면 이 파일객체는 자동으로 사라진다. 
import tempfile
f = tempfile.TemporaryFile()
f.close 
print ()

# time - 시간과 관련된 모듈 
# time.time - 현재시간을 실수 형태로 돌려줌 (1970년 1월 1일 0시 0분 0초 기준) 초단위
import time
print (time.time())

# time.localtime - time.time의 실수 값을 연도,월,일,시,분,초...형태로 바꾸어주는 함수 
print(time.localtime(time.time()))

#time.asctime - time.localtime에 의해서 반한된 튜플형태의 값을 인수로 받아서 알아보기 쉬운 형태로 변환
print(time.asctime(time.localtime(time.time())))

#time.ctime - time.asctime(time.localtime(time.time())) = time.ctime() 이다. 항상 현재시간만 돌려준다.
print(time.ctime())

# time.strtime - 함수에 관계딘 것을 세밀하게 표현하는 여러가지 포맷코드를 제공한다. 
# time.strtime 예시
import time
print(time.strftime("%x", time.localtime(time.time())))
print(time.strftime("%c", time.localtime(time.time())))

# time.sleep - 루프안에서 사용 일정 시간마다 루프를 실행 
"""
실습 3. sleep.py
"""
print ()

# calendar - 파이썬에서 달력을 볼수 있게 해주는 모듈
# calendar.calendar(연도)  그해의 전체 달력 
import calendar
print(calendar.calendar(2023))
# calendar.prcal(연도)를 사용해도 같은 결괏값이다.
# 년,월로 보여주는 예시
print (calendar.prmonth(2023, 7)) 
# calendar.weekday(연도, 월, 일)함수는 그 날짜에 해당하는 요일 정보 출력 / 일 0 ~ 토 6
print (calendar.weekday(2023, 7, 9))

# calendar.monrange (연도, 월) - 입력 받은 달의 1일이 무슨 요일인지와 며칠까지 있는지 튜플로 출력해준다. 
print(calendar.monthrange(2023,7)) # 1일은 금요일 31까지 있음.
print ()

# random - 난수 (규칙이 없는 임의의 수) 발생하는 모듈
import random
print(random.random()) # 0에서 1 사이의 실수

# 1에서 10사사이 정수중 난수
print (random.randint(1,10))
print (random.randint(1,55)) # 1에서 55사이 

"""
실습 4. random_pop.py

"""

# 리스트의 항목을 무작위서 섞고자 할 때,
import random
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
print ()

# webbrowser - 자신이 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈 
# 웹브라우저 자동으로 실행하고, 해당 URL으로 이동 

import webbrowser
webbrowser.open("http://google.com")
# webbrowser.open_new 함수는 이미 실행된 상태여도 새로운 창에 실행이 된다. 
webbrowser.open_new("http://google.com")