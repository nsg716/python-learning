# mod1.py
def add(a,b) :
    return a + b

def sub(a,b) :
    return a - b

# 이런 파일을 모듈이라고 한다. 

# if __name__ == "__main__" 의 의미
if __name__ == "__main__" :
    print (add(1,4))
    print (sub(4,2))
