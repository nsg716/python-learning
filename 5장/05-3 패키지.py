# 패키지(Package) - 도트를 사용하여 파이썬 모둘을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다. 
# 패키지로 만들면 간단한 프로그램이 아닌 이상 유지 보수를 하기에 더 수월하다 

# 패키지 만들기 
# 패키지 기본 구성요소 준비하기 
"""
game 디렉토리 생성 

# game 디렉토리 안에 다음과 같은 파일 생성 

~~~/game/__init__.py
서브 디렉토리 sound 생성
~~~/game/sound/__init__.py
~~~/game/sound/echo.py
서브 디렉토리 graphic 생성
~~~/game/graphic/__init__.py
~~~/game/graphic/render.py

 echo.py, render.py 내용 입력 

 """

# 대화형 인터프리터에 set 함수를 사용해서 PYTHONPATH 환경변수에 
# D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/5장 디렉토리를 추가시킨다. 
"""
D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)/5장>set set PYTHONPATH=D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/5장/game

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)>python

>>>

""" 

# 패키지 안의 함수 실행하기 
# 3 가지 방법이 있다. (import 예제이므로 하나를 실행하면 종료하고 다른 예제를 실행하기)

# 1. echo 모듈을 import 하여 실행하는 방법
"""python
>>> import game.sound.echo         
>>> game.sound.echo.echo_test()    
echo
"""
# 2. echo 모듈이 있는 디렉터리까지를 from...import 하여 실행하는 방법
"""python
>>> from game.sound import echo
>>> echo.echo_test()
echo
"""

# 3. echo 모듈의 echo_test 함수를 직접 import 하여 실행하는 방법
"""python
>>> from game.sound.echo import echo_test
>>> echo_test()
echo

"""
# 도트연산자를 사용해서 import a.b.c 처럼 import를 할 때 가장 마지막 항목인 c 는 반드시 모듈 또는 패키지여야 한다. 

# __init__.py 용도 
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. 

"""python
>>> from game.sound import*
>>> echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined

"""
# 이렇게 특정 디렉토리의 모듈을 * 사용하여 import할 때에는 __init__.py 파일에 __all__변수를 설정하고 import할 수 있는 모듈을 정의해주어야 한다. 

"""
실습1. __init__.py 수정

수정 결과 
D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\5장>python
>>> from game.sound import*
>>> echo.echo_test()        
echo
"""

# relative(관련있는) 패키지 
# 만약 graphic디렉토리의 render.py 모듈이 sound 디렉토리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까?
"""
실습 2. render.py 수정하기 

# 수정 결과 

D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\5장>python
>>> from game.graphic.render import render_test
>>> render_test()
render
echo

# 실습 2 다른 방법 

다른 방법은 부모 디렉토리를 사용하여 import 를 가능하게 하낟. 
..와 같은 relative한 접근자는 render.py 처럼 모듈 안에서만 사용해야 한다. 파이썬 인터프리터에서 사용하면 오류가 발생한다.
""" 