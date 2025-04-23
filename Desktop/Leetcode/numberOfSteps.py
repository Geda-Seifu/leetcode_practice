class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        newnum = num
        while newnum > 0:
            if newnum % 2 == 0:
                newnum = newnum /2
            else:
                newnum = newnum - 1
            count += 1

        return count
solution = Solution()
print(solution.numberOfSteps(14))