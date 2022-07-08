class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target < nums[0]:
            return 0
        elif target > nums[length -1]:
            return length
        elif target not in nums:
            nums.append(target)
            nums.sort()
        
        for i in range(length):
            if nums[i] == target:
                return i