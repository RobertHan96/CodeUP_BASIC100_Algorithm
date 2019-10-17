# 숫자 한개를 입력 받아서 홀/짝 여부, 음수/양수 여부 출력하기


def calc():
    a = int(input())
    if a > 0:
        print('plus')
        if a % 2 == 0:
            print('even')
        elif a % 2 == 1:
            print('odd')
    if a < 0:
        print('minus')
        if a % 2 == 0:
            print('even')
        elif a % 2 == 1:
            print('odd')


calc()
