from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i in range(len(nums)):
            n2 = target - nums[i]

            if n2 in num_dic: 
                return [num_dic[n2], i] 
            
            num_dic[nums[i]] = i  

        return None
    
item = Solution()

print(item.twoSum([2,7,11,15],9))