class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (j < len(nums) - 1) and nums[j] > nums[j + 1]:
                    [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]]
                if j > 0 and nums[i - 1] > nums[i]:
                    [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]]