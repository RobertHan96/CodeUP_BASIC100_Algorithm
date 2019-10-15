# 숫자 두개를 입력받아 비트XOR 연산을 한후 10진수로 출력하는 함수


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    print(a ^ b)


calc()
