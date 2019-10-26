# 정수(1 ~ 100) 1개가 입력되었을 때 하나씩 줄이면서 0까지 카운트다운을 출력해보자.

num = int(input())
while num != 0:
    num = num-1
    print(num)
    if num == 0:
        break
