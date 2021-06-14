def addToArrayForm(num, k):
    carry = 0
    numPointer = len(num)-1
    
    while k!=0 and numPointer>=0:
        sum = num[numPointer] + k %10+carry
        carry=0
        k = k//10
        
        if sum >9:
            num[numPointer]=sum%10
            carry=1
        else: 
            num[numPointer]=sum
            carry=0
        
        numPointer-=1
    
    if carry==1:
        while numPointer>=0 and carry==1:
            sum = num[numPointer]+carry
            if sum>9:
                num[numPointer]=0
            else:
                num[numPointer]+=carry
                carry=0
            numPointer-=1
    
    while k!=0:
      if (k%10+carry)>9:
        num.insert(0,0)
      else:
        num.insert(0,(k%10+carry))
        carry=0
      k=k//10

    if carry==1:
        num.insert(0,1)
    return num

num=[6]
k=809             
print(addToArrayForm(num,k))               
  
        