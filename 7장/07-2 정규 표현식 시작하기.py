# 정규 표현식의 기초, 메타문자
# 메타문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다
# .^$+?{}[]\|()

# 문자 클래스 []
# 문자 클래스로 만들어진 정규식은 "[] 사이에 문자들과 매치"라는 의미이다. 
# 정규표현식이 [abc]이면 'a,b,c 중 한 개의 문자와 매치' 라는 의미를 갖는다.
"""
정규식과 문자열의 매치 
정규식      문자열      매치여부        설명 
              a           Y           'a'는 정규식과 일치하는 문자인 'a' 가 있으므로 매치
[abc]       before        Y           'before'는 정규식과 일치하는 문장인 'b'가 있으므로 매치
            dude          N           정규식과 매치되는 문자가 없다. 매치되지 않다.
"""
# []안의 두문자 사이에 - 를 사용하면 두 문자 사이의 범위이다. 
# 주의해야하는 문자는 ^이다. ^는 Not 의 의미로 반대의 의미이다. 


#Dot(.)
# 정규 표현식의 Dot(.) 메타문자는 줄바꿈 문자는 \n을 제외한 모든 문자와 매치됨을 의미한다. 
# a.b : "a + 모든 문자 + b" 라는 의미이다. 
# a[.]b : "a + Dot(.)문자 + b"

# 반복 (*)
# ca*t : 문자 바로 앞에 있는 a가 0번 이상 반복되면 매치 (ct,cat,caaaat 모두 가능)

# 반복 (+)
# ca+t : 문자 바로 앞에 있는 a가 1번 이상 반복되면 매치 (ct X , cat,caaat 가능 )

# 반복 ({m,n},?)
# 반복횟수를 지정하는 메타문자. 
# 1.{m} : ca{2}t - a가 2번 반복되면 매치 (caat 만 가능 )
# 2.{m,n} : ca{2,5}t - a가 2~5번 반복되면 매치 (cat X, caat,caaaaat 가능 )
# 3. ? : ab?c - b가 0~1번 반복되면 매치 
    # 의미 : "a + b(있어도 되고 없어도 된다. ) + c"


# 파이썬에서 정규 표현식을 지원하는 re 모듈 
import re
p = re.compile("ab*") # 정규표현식을 컴파일한다. re.compile의 결과로 돌려주는 객체 p (컴파일러 패턴 객체)를 사용하여 그 이후의 작업을 수행할 것이다.

# 정규식을 사용한 문자열 검색 
# 컴파일된 패턴 객체는 다음 4가지 메소드를 제공한다. 
"""
메소드          목적
match()     문자열의 처음부터 정규식과 매치되는지 조사한다. 
search()    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall()   정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
finditer()  정규식과 매치되는 모든 문자열을 반복가능한 객체로 되돌려준다.
"""
# macth,search 같은 경우 정규식과 매치될 때는 match 객체를 돌려주고 매치되지 않으면 돌려주지 않는다. 

# 예제 
import re
p = re.compile('[a-z]+') 
m = p.match("python")
print (m) # <re.Match object; span=(0, 6), match='python'> match 객체를 돌려줌
m = p.match("3 python") # 정규식과 부합하지 않는다.
print(m) # None
print ()

"""
p = re.compile(정규 표현식) 
m = p.match("조사할 문자열")
if m : 
    print('Match found : ', m.group())
else :
    print('No match')
match 결괏값이 있을 경우에만 그 다음 작업을 수행한다. 

"""

# search
m = p.search("python")
print (m)
m = p.search("3 python") # 문자열 전체를 검색하기 때문에 정규식과 매치가 된다.  
print (m)

# findall 
result = p.findall("Life is too short") # 정규식과 각각 매치하여 리스트로 돌려준다. 
print (result)

# finduter - 반복 가능한 객체를 돌려준다.
result = p.finditer("Life is too short")
print(result)
for r in result: print (r)

# match 객체의 매서드 

"""
어떤 문자열이 매치되었는가?
매치된 문자열의 인덱스는 어디부터 어디까지인가?

메소드          목적
group()     매치된 문자열을 돌려준다.
start()     매치된 문자열의 시작 위치로 돌려준다.
end()       매치된 문자열의 끝 위치를 돌려준다.
span()      매치된 문자열의 (시작, 끝)에 해당되는 튜플을 돌려준다.
"""
# 예제
import re
p = re.compile('[a-z]+') 
m = p.match("python")
print (m.group())
print (m.start())
print (m.end())
print (m.span())
print()

# search 메소드 사용시 
m = p.search("3 python")
print (m.group())
print (m.start())
print (m.end())
print (m.span())
print()

# 컴파일 옵션 - 정규식을 컴파일 할 때 다음 옵션을 사용할 수 있다.
"""
옵션 이름           약어            설명 
DOTALL              S              dot 문자 (.) 가 줄바꿈 문자를 포함하여 모든 문자와 매치된다.
IGNORECASE          I              대,소문자에 관계없이 매치된다.
MULTILINE           M               여러 줄과 매치된다.
VERBOSE             X               verbose 모드를 사용한다.
"""

# DOTALL, S - 메타문자는 줄 바꿈 문자를 제외한 모든 문자와 매치되는 규칙이 있다. 만약 \n 문자도 포함하여 매치하고 싶다면 
# re.DOTALL or re.S 옵션을 쓰면 된다. 
import re
p = re.compile('a.b')
m = p.match('a\nb')
print (m)
# 옵션 사용
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print (m)

# IGNORECASE, I - 대소문자 구별 없이 매치를 수핼할 때, 사용 
p = re.compile('[a-z]',re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))
print()

#MULTILINE , M - 전체의 처음이 아니라 각 라인의 처음으로 매치하고 싶을 때 사용한다. 
# 미사용 예시 
import re
p = re.compile("^python\s\w+")

data = """python one
life is too start
python two
you need python
python three"""

print (p.findall(data))

# 옵션 사용 예시
p = re.compile("^python\s\w+", re.M)

data = """python one
life is too start
python two
you need python
python three"""

print (p.findall(data))
print ()

# VERBOSE , X - 어려운 정규식을 줄 단위로 끊어서 보기 쉽게 해준다.
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# 옵션 사용
charref = re.compile(r"""
    &[#] # Start of numeric entity reference
    (
    0[0-7]+ # Octal form
    |[0-9]+ # Decimal form
    |x[0-9a-fA-F]+  # Hexadecimal form
    )
    ;         # Trailing semicolon
""", re.VERBOSE) # 주석 처리를 할 수 있으며 기능은 동일한 역할을 할 수 있다. ㄴ
print ()

# 백슬래시 문제 
# 백슬래시를 포함한 정규식 
p = re.compile("\\section") # 하지만 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라 \\ 이 \ 로 변경된다. 
# 해결 방법 
p = re.compile("\\\\section")  # 하지만 이는 복잡한 방법이다. 
# 파이썬 정규식에는 Raw String을 알려줄수 있도록 파이썬 문법을 만든 것이다. 
p = re.compile(r'\\section') # 정규식 문자 앞에 r 문자를 삽입하여 백슬래시 2개 대신 1개만 써도 2개를 쓴것과 동일한 의미를 가진다. 
