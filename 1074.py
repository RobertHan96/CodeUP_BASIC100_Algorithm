# 정수(1 ~ 100) 1개가 입력되었을 때 해당 숫자부터 하나씩 줄이면서 1까지 카운트다운을 출력해보자.

num = int(input())
while num != 0:
    print(num)
    num = num-1
    if num == 1:
        print(num)
        break
