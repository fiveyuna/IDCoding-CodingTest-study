# 백준 / 브론즈2
# 2309 : 일곱 난쟁이
# 30분 

import sys

data = [int(sys.stdin.readline()) for i in range(9)]

# nums = []
# for i in
#   nums.append(int(input()))

total = sum(data) #140
differ = total-100 #40
is_detected = False

for i in range(9):
    pair = differ - data[i] 
    for j in range(1,9):
        if data[j] == pair :
            data.remove(data[i])
            data.remove(data[j-1])
            
            is_detected = True
            break
    
    if(is_detected):         
        break
