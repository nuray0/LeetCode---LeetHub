class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            
        temp = []
        for i in range(4):
            for num in nums:
                if num == i:
                    temp.append(i)
        for i in range(len(nums)):
            nums[i] = temp[i]
            