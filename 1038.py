# 공백으로 구분된 숫자 2개를 입력 받아 합을 출력하는 문제
def plus(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)


num1, num2 = input("숫자 2개를 입력해주세요.").split(' ')

plus(num1, num2)
