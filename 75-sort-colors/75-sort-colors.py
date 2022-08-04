class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """               
        after_0 = 0
        before_2 = len(nums) - 1
        i = 0
        while i <= before_2:
            if nums[i] == 0:
                temp = nums[after_0]
                nums[after_0] = nums[i]
                nums[i] = temp
                after_0 += 1
                i += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[before_2]
                nums[before_2] = temp
                before_2 -= 1
            else:
                i += 1
            