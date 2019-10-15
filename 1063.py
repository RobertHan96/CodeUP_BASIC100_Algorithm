# 삼항연산자를 이용해서 입력받은 숫자 두개 중 큰수를 출력하기


def calc():
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    print(a if a > b else b)


calc()
