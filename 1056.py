# 두개의 숫자를 입력받아 참/거짓이 서로 다를때만 1을 출력하고, 아니면 0을 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a ^ b == 1:
        print(1)
    else:
        print(0)


calc()
