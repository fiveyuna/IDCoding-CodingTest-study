from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    q = deque(people)
    while len(q) > 0:
        cnt += 1
        now = q.pop()

        if len(q) == 0:
            break

        if now + q[0] <= limit:
            q.popleft()

    return cnt

def solution2(people, limit):
    q = deque(people)
    cnt = 0
    while len(q) > 0:
        cnt += 1

        now = q.popleft()
        dif = 300
        other = -1
        for i in range(len(q)):
            if now + q[i] <= limit and dif > abs(now-q[i]):
                dif = abs(now-q[i])
                other = q[i]
        if other != -1:
            q.remove(other)
        

    return cnt

### main ###
case = [70, 50, 80, 50]	
c2 = 100
print(solution(case, c2))
