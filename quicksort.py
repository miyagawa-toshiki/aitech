import random
N = 10
def input_data(data):
    for i in range(N):
        data.append(random.randint(0, N))
    return data
def quicksort(left, right):
    if left >= right:
        return
    else:
        pivot = data[right]
        partition = divition(left, right, pivot)
        quicksort(left, partition - 1)
        quicksort(partition + 1, right)
def divition(left, right, pivot):
    p = 0
    leftnum = left
    rightnum = right - 1
    while left <= right:
        while data[rightnum] >= pivot and rightnum > left:
            rightnum = rightnum -1
        while data[leftnum] <= pivot and leftnum < right:
            leftnum = leftnum + 1
        if leftnum >= rightnum:
            break
        temp = data[leftnum]
        data[leftnum] = data[rightnum]
        data[rightnum] = temp
    temp = data[leftnum]
    data[leftnum] = pivot
    data[right] = temp
    p = leftnum
    return p

if __name__ == "__main__":
    data = []
    data = input_data(data)
    print(data)
    quicksort(0, N-1)
    print(data)