# 코드업 
# 1180 : 만능 휴지통
# 10분

n = int(input())
tens = n // 10
units = n % 10

outcome = ((units*10 + tens)*2) % 100

print(outcome)
if(outcome <= 50) : print("GOOD")
else : print("OH MY GOD")