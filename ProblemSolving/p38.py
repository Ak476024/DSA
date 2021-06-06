def duplicateZeros( arr):
    l=0
    while l<len(arr):
        print(arr,arr[l])

        if arr[l]==0:
            for i in range(len(arr)-1,l,-1):
                arr[i]=arr[i-1]
            
            if l==len(arr)-1:
                arr[l]=0
            l+=2
        else:
          l+=1
A=[0,4,1,0,0,8,0,0,3]
duplicateZeros(A)
print(A)