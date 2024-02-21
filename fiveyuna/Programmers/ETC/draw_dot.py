
def solution(k, d):
    answer = 0
    for y in range(0, d+1, k):
        x = (d**2-y**2)**(1/2) // k + 1
        answer += x
    
    return answer

def solution2(k, d):
    answer = 0
    mid = 0
    for i in range(0,d+1, k):
        for j in range(0,i+1, k):
            if math.sqrt((i*i+j*j)) <= d:
                print(i,j) 
                if i == j:
                    mid += 1
                else :
                    answer += 1
            else:
                break

    return answer*2 + mid

### main ###
#case = [1,2,7,6,4]
print(solution(1,5))