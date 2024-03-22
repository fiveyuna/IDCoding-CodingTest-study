# 백준 / 브론즈2
# 10870 : 피보나치 수 5
# 5분

n = int(input())

first, second = 0, 1
sum = 0
for _ in range(n-1):
    sum = first + second
    first = second
    second = sum
    
if n == 1 :
    sum = 1
print(sum)