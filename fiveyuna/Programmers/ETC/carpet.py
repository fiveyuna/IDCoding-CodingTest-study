

def solution(brown, yellow):
    num = brown + yellow

    for i in range(3,int(num/2)):
        if num % i == 0 and (num//i-2) * (i-2) == yellow:  
            answer = [num//i, i]
            break

    answer.sort(reverse=True)
    return answer

def solution2(brown, yellow):
    num = brown + yellow

    mini = 3000000
    for i in range(1,int(num/2)):
        if num % i == 0:
            dif = abs(num//i-i)
            if mini > dif:
                mini = dif
                answer = [num//i, i]

    answer.sort(reverse=True)
    return answer

### main ###
# case = [1,2,7,6,4]
print(solution(24,24))
