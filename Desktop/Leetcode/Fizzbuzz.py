from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.value = n
        
        result = []
        for n in range(1,int(self.value)+1):
            if n % 3 ==0 and n%5 == 0:
                result.append("Fizzbuzz")
            elif n % 3 == 0:
                result.append("fizz")
            elif n % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(n))

        return result
    



            


