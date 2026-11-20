arr = list(map(int,input("Enter the sort elements :").split()))
goal_ele = int(input("Enter the element to search :"))

left = 0
right = len(arr)-1

found = False

while left <= right:
    mid = (left+right)//2

    if arr[mid] == goal_ele:
        print("Element found at index :",mid)
        found = True
        break

    elif arr[mid] < goal_ele:
        left = mid+1

    else:
        right = mid-1

if not found:
    print("Element is not foumd")   