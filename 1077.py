# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.


def printNums():
    userInput = int(input())
    for i in range(0, userInput+1):
        print(i, sep="")


printNums()
