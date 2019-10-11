# 문자 한개를 입력받아 다음 문자를 출력하는 함수 => 아스키 코드 활용

def nextChar() :
    userInput = input()
    inputAscii = ord(userInput)
    reslut = inputAscii+1
    print(chr(reslut))

nextChar()