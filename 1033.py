#10진수 입력값을 16 진수 대문자로 변환하여 출력하는 예제

inputValue = int(input())
print('{:X}'.format(inputValue))
# 포맷함수를 통한 진수 변환
# {:x} - 16진수, {:b} - 2진수, {:o} - 8진수, {0:0} - 10진수
# 문자를 대문자로 쓰면 출력값의 알파벳도 대문자로 나옴
