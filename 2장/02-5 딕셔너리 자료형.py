#  딕셔너리 : 해시 혹은 연관배열 이라고 한다. Key 와 value 가 있다. 
#  딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요소값을 구하지 않고 Key를 통하여 값을 구할 수 있다.
#  딕셔너리의 예
dic = {'name' : 'pey', 'phone' : '01012345678','birth' : '0101'}
print (dic)
a1 = {1:"hi"} # 정수값을 Key 로 사용항 예시
print (a1) 
a2 = {'a': [1,2,3]} # value에 리스트를 넣을 수 있다.
print (a2)
print ()

# 딕셔너리 쌍 추가, 삭제하기 
# 딕셔너리 쌍 추가하기
a1  = {1:'a'}
a1[2]  ='b' # {2,'b'}쌍 추가 
print (a1)

a1['name'] = 'pey'# name : pey 추가 
print(a1)

a1[3] = [1,2,3] # 3 : [1,2,3] 추가 


# 딕셔너리 요소 삭제하기 
del a1[1] # key 가 1인 key:value 쌍 삭제  / 지정된 key 가 삭제된다.
print (a1)
print()

# 딕셔너리에서 key를 사용해 value 얻기 
a1 = { 2 : 'a', 1 : 'b'}
print (a1[1]) # b가 나온다.
print (a1[2]) # a가 나온다.
##  print (a1['a'])  - 오류 :value를 통해서 찾을 수는 없다. ##

# 딕셔너리를 만들때 주의 사항 
a3 = {1:'a' , 1 : 'c', 1:'b'}
print (a3[1]) # 마지막 key - value 값이 사용되고 그 외의 값은 무시된다. 
# key 에는 리스트는 쓸 수 없지만 튜플은 사용이 가능하다 / 그 이유는 튜플은 고정값이고, 리스트는 값이 변동이 가능하기 때문이다. 
print ()

# 딕셔너리 관련 함수
# Key 리스트 만들기 (keys) 
print(dic.keys()) # dic 의 key 값을 모아서 dict_keys 에 돌려준다.

# 리스트 고유의 함수는 사용할 수 없다.
# 리스트로 변환하기  - 메모리 낭비
print (list(dic.keys())) 

# value 리스트 만들기 (value)
print (dic.values()) # dic 의 value 값을 모아서 dict_values 에 돌려준다.

# Key, value 쌍 얻기 (items)
print(dic.items()) # dic의 Key와 value의 값을 모아서 dict_itmes 객체로 돌려준다.    

# Key : value 값 모두 지우기 (clear)
print (dic.clear()) #None은 존재하지 않음이다.  

# Key 로 value 값 얻기
dic = {'name' : 'pey', 'phone' : '01012345678','birth' : '0101'}
print (dic.get('name')) # a.get('name')의 경우에는 a['name'] 와 같은 방법이다.
print (dic.get('phone')) # 다만 존재하지 않는 key의 경우 None으로 돌려 받는다. 
# 딕셔너리 안에 찾으려는 Key 값이 없는 경우 미리 정해둔 디폴트 값을 가져오게 할 수 있다. - get (x,'디폴트 값')
print (dic.get('xx' , 'bar'))

# Key가 해당 딕셔너리에 조사하기 (in)
print ('name' in dic) # true
print ('xxxx' in dic) # false

