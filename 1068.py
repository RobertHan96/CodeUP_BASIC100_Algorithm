'''
숫자 한개를 입력 받아서 점수에 해당하는 등급 출력하기
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
 0 ~   39 : D
'''


def calc():
    a = int(input())
    if a >= 90:
        print('A')
    elif 70 <= a <= 89:
        print('B')
    elif 40 <= a <= 69:
        print('C')
    else:
        print('D')


calc()
