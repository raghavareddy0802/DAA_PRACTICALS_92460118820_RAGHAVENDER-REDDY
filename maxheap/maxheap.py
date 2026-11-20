arr1 = list(map(int, input("Enter the elements: ").split()))
n = len(arr1)

def heapify(arr1, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr1[left] > arr1[largest]:
        largest = left

    if right < n and arr1[right] > arr1[largest]:
        largest = right

    if largest != i:
        temp = arr1[i]
        arr1[i] = arr1[largest]
        arr1[largest] = temp

        heapify(arr1, n, largest)
for i in range(n // 2 - 1, -1, -1):
    heapify(arr1, n, i)

for i in range(n - 1, 0, -1):

    temp = arr1[0]
    arr1[0] = arr1[i]
    arr1[i] = temp

    heapify(arr1, i, 0)
print("Sorted array:", arr1)