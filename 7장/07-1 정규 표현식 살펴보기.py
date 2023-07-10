# 정규 표현식은 복잡한 문자열을 처리할 때 사용하는 기법 
# 정규표현식의 필요성 

# 문제 : 주민등록번호를 포함하고 있는 텍스트가 있다. 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해보자

""" 정규표현식을 쓰지 않는다면
1. 전체 텍스트를 공백문자로 나눈다. 
2. 나누어진 단어가 주민등록번호 형식인지 확인한다. 
3. 단어가 주민등록번호 형식이라면 뒷자리를 * 로 표시한다. 
4. 나뉜 단어를 다시 조립한다
"""
# 이를 구현한 코드 
data = """
park 800905-1049118
kim  700905-1059119
"""
result = []
for line in data.split("\n") : 
    word_result = []
    for word in line.split(" ") : # 공백문자마다 나누기 
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word [:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result)) # 나눈 단어 조립하기
print ("\n".join(result))

# 정규식을 통해 작성한 코드 
import re # 정규식을 사용하기 위한 모듈 

data = """
park 800905-1049118
kim  700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print (pat.sub("\g<1>-*******", data))

# 정규표현식을 사용하면 간단하게 만들 수 있다. 문자열의 규칙이 복잡할수록 정규식의 호용은 더 커지게 된다. 
