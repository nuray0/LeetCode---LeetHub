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
                if i != after_0:
                    nums[after_0], nums[i] = nums[i], nums[after_0]
                after_0 += 1
                i += 1
            elif nums[i] == 2:
                if i != before_2:
                    nums[before_2], nums[i] = nums[i], nums[before_2]
                before_2 -= 1
            else:
                i += 1
            