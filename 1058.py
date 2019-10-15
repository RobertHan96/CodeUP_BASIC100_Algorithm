# 두개의 숫자를 입력받아 값이 모두 0이면 1을 출력하고, 아니면 0을 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a + b == 0:
        print(1)
    else:
        print(0)


calc()
