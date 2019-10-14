# 두개의 숫자를 입력받아 값이 같으면 1, 다르면 0을 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    if a == b:
        print(1)
    else:
        print(0)


calc()
