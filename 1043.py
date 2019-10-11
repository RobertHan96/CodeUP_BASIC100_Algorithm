#두수를 입력받아 나머지를 출력하는 함수

def modifier() :
    a , b = input().split(' ')
    a = int(a)
    b = int(b)
    reslut = a%b
    print(reslut)

modifier()