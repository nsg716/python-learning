# readline_all.py
f = open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/새 파일.txt",'r')
while True:
    line = f.readline()  # 더이상 읽을 줄이 없으면 None을 출력한다.
    if not line:
        break
    print(line)
f.close()