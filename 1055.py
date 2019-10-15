# 두개의 숫자를 입력받아 하나라도 값이 1이면 1을 출력하고, 아니면 0을 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a or b == 1:
        print(1)
    else:
        print(0)


calc()
