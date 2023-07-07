#range 함수 사용법 

# marks3.py
marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생은 합격입니다." % (number + 1))
# len 함수는 리스틍 안의 요소 개수를 돌려주는 함수이다. 따라서 len(marks)는 5가 될것고, range(5)가 된다. 
# number 변수에 차례대로 0~4 가 대입이 될것이고, marks[number]은 차례로 0~4까지 숫자가 대입될 것이다.