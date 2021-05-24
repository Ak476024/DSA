# Elements which have at-least two greater elements

class FindTwoGreatestElements:
  firstGreatestElement=0
  secondGreatestElement=0


  def find(self,array):

    if len(array)<2:
      return False

    self.firstGreatestElement=max(array[0],array[1])
    self.secondGreatestElement=min(array[0],array[1])

    for element in array[2:]:
      if element>self.firstGreatestElement :
        self.secondGreatestElement=self.firstGreatestElement
        self.firstGreatestElement=element
      elif element>self.secondGreatestElement :
        self.secondGreatestElement= element

    return [self.firstGreatestElement,self.secondGreatestElement]

  def getElements(self,array):
    outputArray=[]
    for x in array:
      if x!= self.firstGreatestElement and x!=self.secondGreatestElement:
        outputArray.append(x)
    return outputArray


inputArray=[99,5,7,2,56,33,21,89]
fge = FindTwoGreatestElements()
print(fge.find(inputArray))
print(fge.getElements(inputArray))