'''
문제 설명    
정수 한 개를 입력받아 1 부터 그 수까지 짝수의 합을 구해보자.

입력
정수 한 개가 입력된다.
(0 ~ 100)
'''

j= 0  
num=int(input())

for i in range(num) :  
    if i%2 == 0 :
        j = j+i
    else : 
        i += 1     
print(j)
