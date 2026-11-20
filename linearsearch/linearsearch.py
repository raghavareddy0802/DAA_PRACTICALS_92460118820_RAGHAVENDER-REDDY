arr = list(map(int,input("Enter the elements : ").split()))
goal_ele = int(input("Enter the element : "))

found = False

for i in range(len(arr)):
    if arr[i] == goal_ele:
          print("Element found at index :",i)
          found = True
          break;

if not found:
     print("Element not found")