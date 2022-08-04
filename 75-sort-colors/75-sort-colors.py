class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """           

        lx = 0
        cx = 0
        rx = len(nums) - 1
        
        while cx <= rx:
            if nums[cx] == 0:
                nums[lx], nums[cx] = nums[cx], nums[lx]
                lx = lx + 1
                cx = cx + 1
            elif nums[cx] == 1:
                cx = cx + 1
            else:
                nums[rx], nums[cx] = nums[cx], nums[rx]
                rx = rx - 1
            