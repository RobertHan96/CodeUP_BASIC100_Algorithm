# 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
# (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.) (x, y축으로 이동하는 2차원 배열 문제임을 알 수 있음)

# 이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

# 미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
# 오른쪽 또는 아래쪽으로만 움직였다.

# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는 (if문 3개 필요)
# 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.


# 미로 상자의 테두리는 모두 벽으로 되어 있으며,
# 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

# 입력
# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.


# 출력
# 성실한 개미가 이동한 경로를 9로 표시해 출력한다.

arrary = []

for i in range(12):
    arrary.append([])
    for j in range(12):
        arrary[i].append(0)
for i in range(10):
    a = input().split()
    for j in range(10):
        arrary[i+1][j+1] = int(a[j])

x = 2
y = 2

while True:
    if arrary[x][y] == 0:
        arrary[x][y] = 9
    elif arrary[x][y] == 2:
        arrary[x][y] = 9
        break
    if((arrary[x][y+1] == 1 and arrary[x+1][y] == 1) or (x == 9 and y == 9)):
        break
    if(arrary[x][y+1] != 1):
        y += 1
    elif(arrary[x+1][y] != 1):
        x += 1


for i in range(1, 11):
    for j in range(1, 11):
        print(arrary[i][j], end=' ')
    print('')
