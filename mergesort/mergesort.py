arr1 = list(map(int, input("Enter the elements: ").split()))

def mergesort(arr1):
    n=len(arr1)
    if len(arr1) <= 1:
        return arr1

    mid = len(arr1) // 2

    left = arr1[:mid]
    right = arr1[mid:]

    left = mergesort(left)
    right = mergesort(right)

    sorted_array = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            sorted_array.append(left[i])
            i = i + 1

        else:
            sorted_array.append(right[j])
            j = j + 1

    while i < len(left):
        sorted_array.append(left[i])
        i = i + 1

    while j < len(right):
        sorted_array.append(right[j])
        j = j + 1

    return sorted_array

sorted_array = mergesort(arr1)

print("Sorted array:", sorted_array)