# 코드업
# 1228 : 비만도 측정 1
# 5분

height, weight = map(float, input().split())
average_weight = (height - 100)*0.9
obesity = (weight - average_weight)*100 / average_weight
outcome = ""

if obesity <= 10 :
    outcome = "정상"
elif (10 < obesity)&(obesity <= 20) :
    outcome = "과체중"
elif obesity > 20 :
    outcome = "비만"
    
print(outcome)
