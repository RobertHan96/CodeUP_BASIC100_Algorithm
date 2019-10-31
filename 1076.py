# 소문자 a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.


def printChar():
    userInput = input()
    inputAscii = ord(userInput)
    i = ord('a')
    while i <= inputAscii:
        print(chr(i), end=" ")
        i += 1


printChar()
