#adddata.py
f = open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/새 파일.txt",'a')
for i in range(11,20): # 11~19까지 대입 
    data = "%d 첫번째 줄입니다.\n" % i
    f.write(data) 
f.close()