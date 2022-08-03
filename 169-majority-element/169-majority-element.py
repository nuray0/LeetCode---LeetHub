import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        max_count = len(nums) // 2
        while True:
            number = random.choice(nums)
            if sum(1 for num in nums if num == number) > max_count:
                return number
