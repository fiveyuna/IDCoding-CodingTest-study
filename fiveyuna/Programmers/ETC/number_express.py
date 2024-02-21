

def solution(n):
    answer = 0

    for i in range(n, 0, -1):
        summ = 0
        for j in range(i, 0, -1):
            summ += j
            if summ == n:
                answer += 1
                break
            if summ > n:
                break
    
    return answer



def solution2(n):
    answer = 0

    
    for i in range(n, 0, -1):
        summ = 0
        for j in range(i, 0, -1):
            summ += j
            if summ == n:
                answer += 1
                break
    
    return answer

### main ###
case = 15
print(solution(case))
