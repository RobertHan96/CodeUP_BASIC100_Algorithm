# 세개의 숫자를 입력받아 합과 평균을 출력하는 함수
# 평균은 소수점 첫째자리까지만 반올림해서 표현

def calc() :
    a , b, c = input().split(' ')
    a = float(a)
    b = float(b)
    c = float(c)
    sum = a+b+c
    avg = (a+b+c)/3

    print(int(sum))
    print(round(avg, 1))

calc()