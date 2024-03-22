# 백준 / 실버5
# 2609 : 최대공약수와 최소공배수
# 45분

a, b = map(int, input().split())

gcf = 1 #최대공약수
lcm = max(a, b) #최소공배수

for i in range(1, min(a, b)+1):
    if (a % i == 0) & (b % i == 0) :
        gcf = i
        
for i in range(1, min(a, b)+1):
    if (lcm*i) % (min(a, b)) == 0 :
        lcm *= i
        break
        
print(gcf, lcm, sep='\n')