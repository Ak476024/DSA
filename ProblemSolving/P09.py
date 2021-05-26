# Count Total Set Bits 1->A

class Bits:

  def countSetBits(self,A):
    count=0
    for i in range(A+1):
      for j in range(32):
        if i%2 !=0:
          count+=1
        i=i>>1
    return count % (pow(10,9)+7)


bits = Bits()
print(bits.countSetBits(3))