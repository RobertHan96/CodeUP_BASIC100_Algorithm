# 입력
# 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
# n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.
# 출력
# 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

# 입력 예시
# 10
# 10 4 2 3 6 6 7 9 8 5
# 출력 예시
# 5 8 9 7 6 6 3 2 4 10


def check():
    n = input("출석 번호를 부른 횟수는?")
    num = input("부르고 싶은 번호를 입력하세요").split()
    n = int(n)

    arrary = []
    for i in range(n):
        arrary.append(int(num[i]))
    index = -1
    count = 0
    while count != n:
        print(arrary[index], end=" ")
        index -= 1
        count += 1


check()
