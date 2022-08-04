class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """               
        mid = 1       # pivot
        i = 0         # less than mid
        j = 0         # current
        k = len(nums) # greater than mid

        while j < k:
            cur = nums[j]
            if cur > mid:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            elif cur < mid:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
            else:
                j += 1
            