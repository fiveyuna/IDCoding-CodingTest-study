# 백준 / 브론즈3
# 2460 : 지능형 기차 2
# 10분


data = [list(map(int, input().split())) for _ in range(10)]

total = 0 
max = 0

for i in range(10) :
   total -= data[i][0]
   total += data[i][1] 
   if max < total :
        max = total

print(max)
