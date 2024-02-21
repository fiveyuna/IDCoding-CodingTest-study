


def solution(s):
    result = []
    for item in list(s):
        if item == ")":
            if len(result) == 0:
                return False
            else:
                result.pop()
        elif item == "(":
            result.append("(")

    if len(result) == 0:
        return True
    else:
        return False


### 간지나게 다시 풀기 ###
def solution2(s):
    result = []
    for item in s:
        if item == ")":
            try:
                result.pop()
            except IndexError:
                return False
        elif item == "(":
            result.append(item)

    return len(result) == 0

### main ###
case = "()()"
print(solution2(case))