# 두개의 수를 입력받아 사칙 연산 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = float(a)
    b = float(b)
    print(int(a+b))
    print(int(a-b))
    print(int(a*b))
    print(int(a//b))
    print(int(a % b))
    print(round(a/b, 2))


calc()
