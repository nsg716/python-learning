# 메타 문자 - 문자열을 위치를 변경하지 않는 메타문자에 대하여 
import re
# | - or 과 동일한 의미 
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
print()

# ^ - 문자열의 맨 처음을 의미한다. 
print (re.search('^Life', 'Life is too short' ))
print (re.search('^Life', 'My Life')) # 처음에 없어서 매치되지 않는다. 
print ()

# $ - 문자열의 맨 마지막을 의미한다.
print (re.search('short$', 'Life is too short'))
print (re.search('short$', 'Life is too short, you need python'))
print ()

# \A 옵션과 상관없이 전체 문자열의 처음하고만 매치한다.
# \Z 옵션과 상관없이 전체 문자열의 끝하고만 매치한다.
# \b - 단어구분자이다., 보통 단어는 whitespace 에 의해 구분된다. 
p = re.compile(r'\bclass\b') # 반드시 r 을 붙여야 한다. 
print (p.search('no class at all')) 
print (p.search('the declassified algorithm')) # class만 있는것이 아니다. 
print (p.search('one subclass is')) # class만 있는것이 아니다. 
print ()

# \B - \b와 정반대의 의미이다. 단어는 whitespace 에 의해 구분된 단어가 아닌 경우에만 매치된다.
p = re.compile(r'\Bclass\B') # 반드시 r 을 붙여야 한다. 
print (p.search('no class at all')) 
print (p.search('the declassified algorithm')) 
print (p.search('one subclass is')) # 앞뒤에 whitespace가 하나라도 있으면 매치가 안된다.
print ()

# 그루핑  - 문자열이 반복되는지 조사하는 정규식 - ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))
print ()
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+") # 전화번호를 찾는 문자 정규식 
m = p.search("park 010-1234-1234")
# 정규식에서 이름만 뽑아내고 싶을 때 
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")  
m = p.search("park 010-1234-1234")
print(m.group(1))

""" 
group (인덱스)        설명 
group(0)            매치된 전체 문자열
group(1)            첫번째 그룹에 해당되는 문자열
group(2)            두번째 그룹에 해당되는 문자열 
group(n)            n 번째 그룹에 해당되는 문자열 

"""
# 전화번호만 뽑아내기 
p = re.compile(r"(\w)+\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))
# 전화번호 국번 만 뽑아내기 
p = re.compile(r"(\w)+\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))
print ()

# 그루핑한 문자열 재참조하기  - 그룹의 또 하나의 좋은 점은 한번 그루핑한 문자열을 재참조가 가능하기 때문이다. 
p = re.compile (r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring').group()
print (m)
print()

# 그루핑된 문자열에 이름 붙이기 
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))
# name 이름이라는 그룹이름으로 참조할 수 있다. 
p = re.compile(r"(?P<word>\w+)\s+(?P=word)")
m = p.search('Paris in the the spring').group()
print (m)
print()

# 전방 탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
print ()
# http: 라는 결괏값에서 : 제외하고 출력하는 것에서 그루핑을 쓸 수 없다고 할 때 전방 탐색을 유용하게 쓸 수 있다. 

"""
정규식      종류                설명 
(?=...)     긍정적 전방 탐색    ...에 해당하는 정규식이 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
(?!...)     부정적 전방 탐색    ...에 해당하는 정규식이 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
"""
# 긍정적 전방 탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
print()

# 부정형 전방 탐색
# 파일 확장자 예시 
#  .*[.].*$ - 파일 확장자 예시 
# .bat 파일을 제외한 확장자 정규식
#  .*([^b].?.?|.[^a]?.?|..?[^t]?)$ - 복잡하다. 이를 해결하는 것이 부정형 전방탐색이다. 
    # - 부정형 전방 탐색 : .*[.](?!bat$).$
    # exe 제외 조건 추가 -   .*[.](?!bat$|exe$).$


# 문자열 바꾸기 - sub 메소드
p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes') # 첫번째 매개변수 바꿀 문자열 , 두번째 매개변수 대상 문자열 
print(m)
# 한번만 바꿀 경우 
m = p.sub('colour', 'blue socks and red shoes', count = 1) # count 를 통해 횟수 조절
print(m)
print ()

# sub 메소드를 사용할 때 참조구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print (p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 이름 + 전화번호 를 전화번호 + 이름으로 바꾸는 예이다. / \g<그룹이름>을 사용하면 정규식의 그룹 이름을 참조할 수 있다.
# 참조번호도 마찬가지이다. 
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print (p.sub("\g<2> \g<1>", "park 010-1234-1234"))
print()

# sub 메서드의 매개변수로 함수 넣기 
def hexrepl(match):
    value = int (match.group())
    return hex(value)
p = re.compile(r'\d+') # 숫자와 매치되면 그 값을 16진수로 바꾸어서 다시 반환값으로 바꾸어 넣는다.
m = p.sub(hexrepl, "Call 65490 for printting, 49152 for user code.")
print (m)
print ()

# Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>',s).span())# *가 탐욕스러워서 모든 문자열을 돌려버렸는데 이를 조정하는 방법이다. 
print(re.match('<.*>',s).group())
# Non-Greedy 문자인 ? 를 사용하면 * 탐욕을 억제할 수 있다.
print(re.match('<.*?>',s).group()) # 가능한 가장 최소한의 반복을 수행하도록 하는 것이다.

# 완