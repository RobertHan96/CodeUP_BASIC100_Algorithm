# 1부터 n까지, 1부터 m까지 숫자가 적힌
# 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.

a, b = input().split()
a = int(a)
b = int(b)
for n in range(1, a+1):
    for m in range(1, b+1):
        print(n, m)
