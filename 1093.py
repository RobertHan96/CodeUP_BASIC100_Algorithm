# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

# 출력
# 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.


def check():
    n = input("출석 번호를 부른 횟수는?")
    num = input("부르고 싶은 번호를 입력하세요").split()
    n = int(n)

    arrary = []
    for i in range(24):
        arrary.append(0)
    for i in range(n):
        arrary[int(num[i])] += 1
    for i in range(1, 24):
        print(arrary[i], end=" ")


check()
