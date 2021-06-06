# letter Phone

def letterPhone(digits):
  result=[]
  if len(digits) == 0 or digits==None:
    return result

  mappings = [
    "0",
    "1",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
  ]

  letterCombinationRecursive(result,digits,"",0,mappings)
  return result

def letterCombinationRecursive(result, digits, current, index, mappings):
  if index == len(digits):
    result.append(current)
    return

  letters = mappings[int(digits[index])]
  for i in letters:
    letterCombinationRecursive(result,digits,current+i, index+1,mappings)

print(letterPhone("231"))
