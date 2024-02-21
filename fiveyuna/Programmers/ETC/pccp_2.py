from collections import deque

mx, my, group_cnt = 0, 0, 0
visited, group = {}, {}
DIR = [(0,-1), (0, 1), (1,0), (-1,0)]

def bfs(x, y, vis, land):
    global mx,my,group_cnt, DIR
    
    count = 1
    q = deque([(x,y)])
    visited[(x,y)] = group_cnt

    while q:
        x,y = q.popleft()

        for dx, dy in DIR:
            nx, ny = x + dx, y + dy

            if 0 <= nx < mx and 0 <= ny < my and land[ny][nx] != 0 and (nx, ny) not in vis:
                vis[(nx,ny)] = group_cnt
                q.append((nx,ny))
                count += 1

    group[group_cnt] = count
    group_cnt += 1


def solution(land):
    global mx,my, group, visited
    mx, my = len(land[0]), len(land)

    for y in range(my):
        for x in range(mx):
            if (x,y) not in visited and land[y][x] == 1:
                bfs(x,y, visited, land)

    answer = 0
    for x in range(mx):
        already = []
        summ = 0
        for y in range(my):
            if land[y][x] != 0:
                group_cnt = visited[(x,y)]
                if group_cnt in already:
                    continue
                else:
                    summ += group[group_cnt]
                    already.append(group_cnt)
        if answer < summ:
            answer = summ
    
    return answer



### main ###
#case = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
case = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(case))