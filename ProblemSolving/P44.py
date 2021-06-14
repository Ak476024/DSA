
A=1702766719


def isBadVersion(n):
  if n >=A:
    return True
  return False

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    l=1
    r= n
    count=0
    while(l<=r):
        mid = l+r//2
        print(mid)
        temp=isBadVersion(mid)
        print(temp)
        if temp==True :
            print(mid,l,r)
            if isBadVersion(mid-1)==False:
                return mid
            else:
                r=mid-1
        else :
            if isBadVersion(mid+1)==True:
                return mid+1
            else:
                l=mid+1
        count+=1
print(firstBadVersion(2126753390))