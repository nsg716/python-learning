#D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)\6장/ tabto.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src) # a.txt 파일을 읽어 들임
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4) # 탭을 공백 4개로 변환

f = open(dst, 'w') # 변경된 내용을 b.txt 파일을 통해서 확인이 가능하다.
f.write(space_content)
f.close()
