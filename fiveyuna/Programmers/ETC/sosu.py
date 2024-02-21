answer = 0

def is_prime(num):
    global answer
    for i in range(2, num):
        if num % i == 0:
            return
    answer += 1
    return

def check_case(idx, nums):
    for i in range(idx+1, len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[idx] + nums[i] + nums[j]
            is_prime(sum)


def solution(nums):
    global answer

    for i in range(len(nums)):
        check_case(i, nums)

    return answer

### main ###
case = [1,2,7,6,4]
print(solution(case))