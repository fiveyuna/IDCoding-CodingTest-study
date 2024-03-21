# 코드업
# 1163 : 당신의 사주를 봐 드립니다 2
# 5분

year, month, date = map(int, input().split())
output = "그럭저럭"
num = (year + month + date)//100

if(num % 2 == 0):
    output = "대박" 
    
print(output)