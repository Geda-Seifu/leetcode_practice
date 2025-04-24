class Solution:
    def reverse(self, x: int) -> int:
        rev=0;
        is_negative = x < 0
        x = abs(x)

        
        while x>0:
            rev = rev*10 + x%10          
            x//=10

        if is_negative:
            rev = -rev 

        if rev <= -2**31 or rev >= 2**31 -1:
            return 0


        return rev 
    

item = Solution()
print(item.reverse(8989898989898))