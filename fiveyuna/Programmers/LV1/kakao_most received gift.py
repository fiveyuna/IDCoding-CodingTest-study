giveDic = {}
giftNumDic = {} 
answerDic = {}

# calculate people's give list -> giveDic, giftNumDic
def find_gifts(name, giftList):
    giveList = []
    
    # TODO : name 없으면 추가하는 방식
    for g in giftList:
        gInfo = g.split() # ex.[muzi,frodo]
        if name == gInfo[0]:
            giveList.append(gInfo[1]) # 선물 준 사람 리스트에 추가
            giftNumDic[name] += 1 # 준 사람 선물 지수 +1
            giftNumDic[gInfo[1]] -= 1 # 받은 사람 선물 지수 -1
        
    giveDic[name] = giveList
    return 

# Final calculation -> answer dictionary
def calc_gifts(p1, p2):
    p1Gives = giveDic[p1]  
    p2Gives = giveDic[p2]

    if p1Gives.count(p2) > p2Gives.count(p1):
        answerDic[p1] +=1
    elif  p1Gives.count(p2) < p2Gives.count(p1):
        answerDic[p2] +=1
    else:  # same -> 선물 지수 큰 사람 +1
        if giftNumDic[p1] > giftNumDic[p2]:
            answerDic[p1] +=1
        elif giftNumDic[p1] < giftNumDic[p2]:
            answerDic[p2] +=1
        else:
            return
        
    return

def solution(friends, gifts):
    # Initialize
    for f in friends:
        answerDic[f] = 0
        giftNumDic[f] = 0

    # Gift Dictionary & Gift number
    for f in friends:
        find_gifts(f, gifts)

    # Final calculation
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            calc_gifts(friends[i], friends[j])

    answerList = answerDic.values()
    return max(answerList)

##### main #####
print(solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))