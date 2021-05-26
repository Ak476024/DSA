# Add Binary Strings

class BinaryString:

  def add(self,firstString,secondString):
    carry = 0
    sum = ""
    firstStringLength = len(firstString)
    secondStringLength = len(secondString)

    if firstStringLength>secondStringLength:
      secondString = "0"*(firstStringLength-secondStringLength)+secondString
    else:
      firstString = "0"*(secondStringLength-firstStringLength)+firstString

    length = len(firstString)

    for index in range(length):
        temp= int(firstString[length-index-1])+int(secondString[length-index-1])+carry
        sum = str(temp%2)+sum
        carry = int(temp/2)
    return sum

binaryString = BinaryString()
print(binaryString.add("1010110111001101101000","1000011011000000111100110"))