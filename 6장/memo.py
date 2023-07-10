# D:\코드 배움\Python 코드 배움\파이썬 폴더 (테스트 용)/6장/memo.py
import sys

option = sys.argv[1] # 실행 옵션값

if option == '-a': # 옵션이 -a인경우에만 memo 값을 읽어 memo.txt 파일에 그 값을 쓰도록 코드를 작성 
    memo = sys.argv[2] # 메모 내용
    f = open('memo.txt', 'a') # 한줄 씩 추가하는 것이므로 모드는 a
    f.write(memo)
    f.write('\n') # 메모를 추가할 때 마다 다음 줄에 저장되도록 설정 
    f.close()
elif option == '-v': # 옵션으로 -v 가 들어온 경우 memo.txt 파일을 읽어서 출력한다. 
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)



# sys.argv[0]은 memo.py이므로 필요가 없다. 
