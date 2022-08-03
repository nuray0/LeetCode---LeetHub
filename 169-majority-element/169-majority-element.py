

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        half = len(nums) // 2
        if half == 0:
            return nums[0]
        
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
                if counts[num] > half:
                    return num
