# 두개의 숫자를 입력받아 앞의수가 크면1, 뒤에수가 크면 0을 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a > b:
        print(1)
    else:
        print(0)


calc()
