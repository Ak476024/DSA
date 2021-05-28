# FizzBuzz
# Multiples 3->Fizz 5->Buzz 3&5->FizzBuzz

class FizzBuzz:

  def print(self, x):
    for x in range(x+1)[1:]:
      if x%3==0 and x%5==0:
        print("FizzBuzz", end=" ")
      elif x%5==0:
        print("Buzz", end=" ")
      elif x%3==0:
        print("Fizz", end=" ")
      else:
        print(x, end=" ")

fz=FizzBuzz()
fz.print(20)