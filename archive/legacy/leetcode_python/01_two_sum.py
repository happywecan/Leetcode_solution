from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        for idx,num in enumerate(nums):
            complement =  target - num
            if complement in num_map:
                return [num_map[complement],idx]
            else:
                num_map[num] = idx
        return []        