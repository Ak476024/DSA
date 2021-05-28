#Odd Even Subsequences
A=[1, 2,2,3]
class OddEvenSubsequences:

  def maxLength(self, A):
    toggle = "odd" if A[0]%2==0 else "even"
    B=[A[0]]
    for i in range(len(A))[1:]:
      if (A[i]%2!=0 and toggle == "odd") or(A[i]%2==0 and toggle == "even"):
        B.append(A[i])
        toggle= "odd" if toggle=="even" else "even"
    return B

oddEven =OddEvenSubsequences()
print(oddEven.maxLength(A))