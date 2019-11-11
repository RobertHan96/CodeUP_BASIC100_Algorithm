# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
# 방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)
#     출력
#     3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

a, b, c = input().split()

A = int(a)
B = int(b)
C = int(c)
days = 1

while days % A != 0 or days % B != 0 or days % C != 0:
    days += 1


print(days)
