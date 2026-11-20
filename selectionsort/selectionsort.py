arr1 = list(map(int,input("Enter the elements :").split()))
n = len(arr1)

for i in range(n):
    mini = i
    for j in range(i+1,n):
        if arr1[j] < arr1[mini]:
            mini = j

    temp = arr1[i]
    arr1[i] = arr1[mini]
    arr1[mini] = temp

print("sorted array :",arr1)