# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 예
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall


def season():
    month = input("원하는 달을 숫자를 입력해주세요")
    month = int(month)
    if 1 <= month <= 2:
        print("winter")
    if 3 <= month <= 5:
        print("spring")
    if 6 <= month <= 8:
        print("summer")
    if 9 <= month <= 11:
        print("fall")
    if month == 12:
        print("winter")


season()
