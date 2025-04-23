class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        middle = 0
        while x > middle:
            middle = middle*10 + x%10
            x=x//10

        return x == middle or x == middle//10
    
item = Solution()

print(item.isPalindrome(121121))