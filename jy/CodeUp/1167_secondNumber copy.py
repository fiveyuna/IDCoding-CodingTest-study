# 세 개의 숫자가 주어질 때 작은 순서로 나열 했을 때, 두번째 수를 출력
# 입력예시) 201 20 3
# 출력예시) 20

str = input()
list = list(map(int, str.split()))

# 버블정렬
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubbleSort(list)

print(list[1])