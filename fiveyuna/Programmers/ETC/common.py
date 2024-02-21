### main ###
case = [1,2,7,6,4]
print(solution(case))

### Utillity ###
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return
    return

### 조합 
def check_case(idx, nums):
    for i in range(idx+1, len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[idx] + nums[i] + nums[j]
            is_prime(sum)

### 재귀 런타임 에러
import sys
sys.setrecursionlimit(10000)