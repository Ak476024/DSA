def merge( nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1=0
    p2=0
    
    while p1<m and p2<n:
        print(p1,p2,nums1)

        if nums1[p1] <= nums2[p2]:
            p1+=1
        elif nums1[p1]>nums2[p2]:
            for i in range(m+n-1,p1-1,-1):
                nums1[i]= nums1[i-1]
                print(nums1)
            nums1[p1]=nums2[p2]
            print(nums1,p1,p2)
            p1+=2
            p2+=1
    print(p1,p2)
    while(p2<m):
        nums1[p1]=nums2[p2]
        p2+=1
        p1+=1    

nums1=[2,0,0]
m=1
nums2=[1,3]
n=2
merge(nums1, m,nums2, n)   
print(nums1)
     