# 세 수를 오름차순으로 정렬
# 입력예시) 8 7 6
# 출력예시) 6 7 8

str = input()
list = list(map(int, str.split()))

# 삽입정렬
def insertSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
            
insertSort(list)

print(*list)