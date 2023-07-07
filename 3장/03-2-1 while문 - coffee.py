#coffee.py
"""
coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300 :
        print ("커피를 받습니다.")
        coffee = coffee -1 
    elif money > 300 :
        print("거스름돈 %d 를 돌려주고, 커피를 받습니다." %(money -300))
        coffee = coffee -1
    else :
        print ("돈이 부족하여 커피를 주지 않습니다.")
        print ("남은 커피의 양은 %d 개입니다."  % coffee)
        if coffee == 0:
            print ("커피가 다 떨어졌습니다. 판매를 중지합니다.") 
            break

"""
### 중간에 커피의 개수가 음수로 변하였으나 계속 명령이 실행이 된다. 이를 고치다면 다음과 같이 된다. (original)

## 수정본
coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    
    if money == 300 :
        print ("커피를 받습니다.")
        coffee = coffee -1 
        print ("남은 커피의 양은 %d 개입니다."  % coffee) # 편의성
        if coffee == 0:
            print ("커피가 다 떨어졌습니다. 판매를 중지합니다.")  
            break
    elif money > 300 :
        print("거스름돈 %d 를 돌려주고, 커피를 받습니다." %(money -300))
        coffee = coffee -1
        print ("남은 커피의 양은 %d 개입니다."  % coffee) # 편의성
        if coffee == 0:
            print ("커피가 다 떨어졌습니다. 판매를 중지합니다.")  
            break
    else :
        print ("돈이 부족하여 커피를 주지 않습니다.")
        print ("남은 커피의 양은 %d 개입니다."  % coffee)
        
           