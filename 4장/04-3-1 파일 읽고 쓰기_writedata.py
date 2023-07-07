# writedata.py
f = open("D:/코드 배움/Python 코드 배움/파이썬 폴더 (테스트 용)/4장/새 파일.txt",'w')
for i in range(1,11):
    data = "%d 줄입니다.\n" %i
    f.write(data) # data 파일 객체 f 에 써라 
f.close()
# 새 파일에 해당하는 함수의 결괏값이 출력되었다. 
for i in range(1,11):
    data = "%d 줄입니다.\n" %i
    print(data)
    # 모니터 출력 