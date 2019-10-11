from time import localtime, strftime
time = list(input("시간을 입력해주세요."))

minute = time[3:5]
outputminute =list(map(str, minute)) #map함수 사용시 list도 형변환 쉽게 가능
finalminute = outputminute[0] + outputminute[1]

print(finalminute)
