# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 100)
#     출력
#     n번째 수를 출력한다.


a, d, n = input().split()

A = int(a)
D = int(d)
N = int(n)

for i in range(N-1):
    A = A + D

print(A)
