
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        
        if len(nums) == 0 or len(nums) ==1:
            return len(nums)
        
        while fast < len(nums):      
		# fast pointer found distinct element so increment slow pointer and assign value which is at fast pointer.
            if nums[slow] < nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1