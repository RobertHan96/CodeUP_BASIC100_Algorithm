# 출력
# 출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.

# 입력 예시
# 10
# 10 4 2 3 6 6 7 9 8 5

# 출력 예시
# 2


n = input("출석 번호를 부른 횟수는?")
num = input("부르고 싶은 번호를 입력하세요").split()
n = int(n)

arrary = []
for i in range(n):
    arrary.append(int(num[i]))
min = max(arrary)

for i in range(n):
    if arrary[i] < min:
        min = arrary[i]

print(min)
