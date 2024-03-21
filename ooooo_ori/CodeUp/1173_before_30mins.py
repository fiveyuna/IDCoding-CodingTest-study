# 코드업 
# 1173 : 30분전
# 분 58~

hour, minute = map(int, input().split())

if(minute < 30):
    if(hour == 0) : hour = 23
    else : hour -= 1
    
minute = (minute + 30) % 60

print(str(hour) + ' ' +str(minute))