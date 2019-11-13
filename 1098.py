
# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
#     막대를 놓는 방향(d:가로는 0, 세로는 1)
# 입력값의 정의역은 다음과 같다.

# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1
# 1 <= x <= 100-h
# 1 <= y <= 100-w


# 출력
# 모든 막대를 놓은 격자판의 상태를 출력한다.
# 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
# 단, 각 숫자는 공백으로 구분하여 출력한다.

h, w = input("판의 세로 크기, 가로 크기 입력 : ").split()
h, w = int(h), int(w)
arrary = []
n = int(input("막대의 개수 입력 :"))

for i in range(h):
    arrary.append([])
    for j in range(w):
        arrary[i].append(0)


for i in range(n):
    l, d, x, y = input("막대의 길이, 방향(0은 가로, 1은 세로), x좌표, y좌표 입력 : ").split()
    for j in range(int(l)):
        if int(d) == 0:
            arrary[int(x)-1][int(y)-1+j] = 1
        else:
            arrary[int(x)-1+j][int(y)-1] = 1
for i in range(h):
    for j in range(w):
        print(arrary[i][j], end=' ')
    print('')
