# 입력
# 시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 10)
#     출력
#     n번째 수를 출력한다.

a, r, n = input().split()

A = int(a)
R = int(r)
N = int(n)

for i in range(N-1):
    A = A * R

print(A)
