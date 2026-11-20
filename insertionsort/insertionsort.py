arr1 = list(map(int,input("Enter thr elements :").split()))
n = len(arr1)

for i in range(1,n):
    key = arr1[i]
    j = i-1

    while j >= 0 and arr1[j] > key:
        arr1[j+1] = arr1[j]
        j = j-1

    arr1[j+1] = key
print("sorted arrt :",arr1)