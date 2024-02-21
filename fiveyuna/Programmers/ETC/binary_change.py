def to_binary(n):
    num = ""
    while n >= 1:
        num += str(int(n % 2))
        n /= 2
    
    result = ""
    for i in range(len(num)-1, -1, -1):
        result += num[i]

    return result

def solution(s):
    answer = [0, 0] # cnt, zero cnt
    bi = s
    while len(bi) > 1:
        answer[1] += bi.count("0")
        bi = bi.replace("0","")
        print("1. " + bi)
        bi = to_binary(len(bi))
        print("2. " + bi)
        answer[0] += 1
    return answer

### main ###
case = "110010101001"

print(solution(case))
