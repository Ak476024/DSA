#Example: For A = 3 pattern looks like:
# 1
# 1 2
# 1 2 3

class PatternBuilder:
   def buildPatter(self,number):
     outputArray=[]
     for row in range(number+1)[1:]:
       colArray=[]
       for column in range(row+1)[1:]:
          colArray.append(column)
       outputArray.append(colArray)
     return outputArray


patternbuilder = PatternBuilder()
print(patternbuilder.buildPatter(5))