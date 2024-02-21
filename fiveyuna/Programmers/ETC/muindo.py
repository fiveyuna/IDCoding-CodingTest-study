import sys

new_map = []
y_len = 0
x_len = 0
memo = {}

sys.setrecursionlimit(10000)

def find(i,j):
    if i<0 or i>=y_len or j<0 or j>=x_len:
        return 0
    if new_map[i][j] == 'X':
        return 0
    if str(i)+","+str(j) in memo:
        return memo[str(i)+","+str(j)]
    
    val = int(new_map[i][j])
    new_map[i][j] = 'X'
    memo[str(i)+","+str(j)] = val + find(i-1,j) + find(i+1,j) + find(i,j-1) + find(i,j+1)
    return memo[str(i)+","+str(j)]


def solution(maps):
    answer = []

    global y_len, x_len
    y_len = len(maps)
    for m in maps:
        new_map.append(list(m))
    x_len = len(list(m))

    for i in range(y_len):
        for j in range(x_len):
            res = find(i,j)
            if res != 0:
                answer.append(res)
    
    answer.sort()

    if len(answer) == 0:
        answer.append(-1)

    return answer


### main ###
case = ["X591X","X1X5X","X231X", "1XXX1"]	
print(solution(case))

