def solution(bandage, health, attacks):
    now_h = health
    con_h = 0

    band_time = bandage[0]
    band_heal = bandage[1]
    band_plus = bandage[2]

    max_time = attacks[len(attacks)-1][0]
    att_dic = {}
    for att in attacks:
        att_dic[att[0]] = att[1]

    for t in range(1, max_time+1):
        print(now_h)
        if t in att_dic:
            now_h -= att_dic[t]
            con_h = 0
        else:
            now_h += band_heal
            con_h += 1
            if con_h == band_time:
                now_h += band_plus
                con_h = 0
            if now_h > health:
                now_h = health
    
        if now_h <= 0:
            return -1
    return now_h

### main ###
p1 = [10,10,100]
p2 = 10
p3 = [[1,15],[3,1]]
print(solution(p1,p2,p3))

# bandage는 [시전 시간, 초당 회복량, 추가 회복량]
# attacks[i]는 [공격 시간, 피해량] 