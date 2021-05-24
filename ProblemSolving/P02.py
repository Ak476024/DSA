# MINIMUM PICKS
# Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.

class MinimumPick:

  maxEven=None
  minOdd=None

  def findMinOddAndMaxEven(self,array):

    if len(array)<2:
      return False

    for element in array:
      if element%2 == 0:
        if self.maxEven is None:
          self.maxEven=element
        self.maxEven=max(self.maxEven,element)
      else:
        if self.minOdd is None:
          self.minOdd=element
        self.minOdd= min(self.minOdd,element)

    return
  
  def getDiff(self):
    return self.maxEven - self.minOdd

inputArray=[0, 2, 9]
minPack =MinimumPick()
minPack.findMinOddAndMaxEven(inputArray)
print(minPack.getDiff())