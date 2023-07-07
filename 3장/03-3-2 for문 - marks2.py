# for문에서 continue도 사용이 가능하다. for 문을 수행하는 도중 contnue를 만나면 for문의 처음으로 돌아가게 된다. 
# marks2.py
marks = [90,25,67,45,80]
number = 0  # 학생에게 붙여줄 번호
for mark in marks : 
    number = number + 1
    if mark < 60  : # 점수가 60점 미만일 경우 if문 수행 
        continue     
    print("%d번 학생은 합격입니다." % number)