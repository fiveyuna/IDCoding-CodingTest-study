# 코드업
# 1162 : 당신의 사주를 봐 드립니다 1
# 10분

year, month, date  = map(int, input().split())
output = "그럭저럭"

num = year - month + date
if num % 10 == 0 :
    output = "대박"
    
print(output)