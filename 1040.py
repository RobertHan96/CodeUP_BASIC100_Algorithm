# 입력받은 정수의 부호를 바꿔서 출력하기


def chagneSign(num):
    num = int(num)
    if num >= 0:
        print(num*-1)
    else:
        print(abs(num))


userInput = input()
chagneSign(userInput)
