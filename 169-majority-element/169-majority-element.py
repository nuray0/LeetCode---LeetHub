class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        max_count = 0
        max_num = nums[0]
        for key, count in counts.items():
            if count > max_count:
                max_count = count
                max_num = key
        return max_num