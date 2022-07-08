class Solution:

    
    def maxSubArray(self, nums: List[int]) -> int:
        currMax=globalMax=nums[0]
        for i in range(1,len(nums)):
            currMax=max(nums[i],currMax+nums[i])
            if currMax>globalMax:
                globalMax=currMax
        return globalMax  
        