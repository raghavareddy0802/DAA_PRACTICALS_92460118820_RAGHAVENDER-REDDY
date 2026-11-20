arr1 = list(map(int, input("Enter the elements: ").split()))

def quick_sort(arr1):

    if len(arr1) <= 1:
        return arr1

    pivot = arr1[0]

    left = []
    right = []

    for i in range(1, len(arr1)):

        if arr1[i] < pivot:
            left.append(arr1[i])

        else:
            right.append(arr1[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

sort_array = quick_sort(arr1)
print("Sorted array:", sort_array)          