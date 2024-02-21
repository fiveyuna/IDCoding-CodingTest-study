def solution(s):
    list_a = list(map(int, s.split()))
    # print(list_a)
    return str(min(list_a)) + " " + str(max(list_a))

### main ###
case = "-1 -2 -3 -4"
print(solution(case))