# Given an array of integers A, every element appears twice except for one. Find that single one.

class SingleElement:

  def find(self,inputArray):
    output=0
    for i in inputArray:
      output ^= i
    return output

inputArray=[1,5,6,3,4,5,6,3,1]
singleElement = SingleElement()
print(singleElement.find(inputArray))