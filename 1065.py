# 숫자 세개를 입력 받아서 짝수만 출력하기


def calc():
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    if a % 2 == 0:
        print(a)
    if b % 2 == 0:
        print(b)
    if c % 2 == 0:
        print(c)


calc()
