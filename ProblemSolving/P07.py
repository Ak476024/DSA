# Single Number II

# Given an array of integers, every element appears thrice except for one which occurs once.

class SingleElement:

  def find(self,inputArray):
    element=0
    for i in range(32):
      sumBit=0
      for j in inputArray:
        j=j>>i
        sumBit += j%2
      
      element+=pow(2,i)*(sumBit %3)
    return element

inputArray=[1,1,1,2,2,2,3,3,3,4]
singleElement = SingleElement()
print(singleElement.find(inputArray))