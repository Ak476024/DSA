# Reverse Bits

class ReverseBit:

  def reverse(self,A):
    B=0
    for i in range(32):
      bit = A % 2
      B = B << 1
      B = B + bit
      A = A >> 1
    return B


reverseBit = ReverseBit()
print(reverseBit.reverse(1))