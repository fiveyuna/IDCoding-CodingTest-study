# 코드업 
# 1166 : 윤년 판별
# 10분

N = int(input())
output = "Normal"

if(N % 400 == 0):
    output = "Leap"
elif((N % 4 == 0) & (N % 100 != 0)):
    output = "Leap"

print(output)