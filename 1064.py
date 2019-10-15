# 삼항연산자를 이용해서 입력받은 숫자 세개 중 가장 작은수를 출력하기
# 문제 풀이 보류


def calc():
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    print((a if a < b else b) and (c if c < b else b))


calc()
