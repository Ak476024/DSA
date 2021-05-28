#Odd Even Subsequences
class OddEvenSubsequences:

  def maxLength(self, A):
    toggle = "odd" if A[0]%2==0 else "even"
    pointer=1
    for i in range(len(A))[1:]:
      if (A[i]%2!=0 and toggle == "odd") or(A[i]%2==0 and toggle == "even"):
        A[pointer]=A[i]
        pointer+=1
        toggle= "odd" if toggle=="even" else "even"
    del A[pointer:]
    print(pointer)
    return A

oddEven =OddEvenSubsequences()
A=[2,9,2,2,3,4]
print(oddEven.maxLength(A))