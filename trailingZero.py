class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n>0:
            n//=5
            count+=n
        return count
    

item = Solution()

print(item.trailingZeroes(25))
