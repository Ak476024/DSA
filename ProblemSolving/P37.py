def findPairs(nums, k):
    result=[]
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            print(nums[j],sum)
            if sum==k:
                result.append(A[i:j+1])
                break
            if sum> k:
                break
    
    return result

A=[1,-1,0]
k=0
print(findPairs(A,k))