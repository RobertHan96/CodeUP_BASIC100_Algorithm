# 숫자 세개를 입력 받아서 각수의 홀수 또는 짝수 여부 출력하기


def calc():
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    if a % 2 == 0:
        print('even')
    elif a % 2 == 1:
        print('odd')
    if b % 2 == 0:
        print('even')
    elif b % 2 == 1:
        print('odd')
    if c % 2 == 0:
        print('even')
    elif c % 2 == 1:
        print('odd')


calc()
