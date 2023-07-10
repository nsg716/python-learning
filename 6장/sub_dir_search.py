# D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장/sub_dir_search.py

def search(dirname) :
    print (dirname)

search("D:/")# 시작 디렉토리를 입력받도록 코드를 작성했다.
""" 실습을 위해서 주석 처리
# 디렉토리에 있는 파일을 검색할 수 있도록 소스 변경 
import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname,filename)
        print(full_filename)
search("D:/")
"""
"""
D:/
D:/!!!#1(4323871)
D:/!!!#1(5466891)
D:/!!!#1(8914207)
D:/$RECYCLE.BIN
D:/%K&CV0A
D:/Common
D:/Config.Msi
D:/C언어 연습
D:/Recovery
D:/System Volume Information
D:/Users
D:/visual studio
D:/VsWebProtocolSelector
D:/영상 저장
D:/영상녹화 앱(프로그램)
D:/코드 배움
"""

# 확장자가 .py 파일만을 출력하고록 코드를 변경 

import os

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname,filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)
search("D:/")

"""
D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장>C:/Users/1029c/AppData/Local/Programs/Python/Python311/python.exe "d:/코드 배움/Python 코드 배움/파이
썬 폴더 (테스트 용)/6장/sub_dir_search.py"
D:/

"""

# 그 하위디렉토리를 포함한 모든 파이썬 파일을 검색하는 것 

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)
            if os.path.isdir(full_filename) :
                search(full_filename)
            else : 
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError : 
        pass
search("D:/") 

# 모든 파일을 출력할 수 있으나  렉이 걸리니 주의 