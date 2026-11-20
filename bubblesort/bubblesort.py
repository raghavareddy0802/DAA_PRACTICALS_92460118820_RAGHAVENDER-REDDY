arr1 = list(map(int,input("Enter the elements :").split()))
n = len(arr1)

for i in range(n):
   for j in range(0,n-i-1):
      if arr1[j] > arr1[j+1]:

         temp = arr1[j]
         arr1[j] = arr1[j+1]
         arr1[j+1] = temp 

print("sorted array:",arr1)