# All Unique Permutations

# Input: A = [1, 1, 2]
# Output: 
# [1,1,2]
# [1,2,1]
# [2,1,1] 

def Permutation(A,length,count,prefix):
  if len(prefix) == length:
    count.append(prefix)
  
  for i in A.keys():
    if A[i]>0:
      B= A.copy()
      B[i]-=1
      Permutation(B,length,count, prefix=prefix+[i])
  return

A=[1, 2, 3]
B={}

for i in A:
  if i in B:
    B[i]+=1
  else:
    B[i]=1
    
count=[]
Permutation(B,len(A),count,[])
print(count)
