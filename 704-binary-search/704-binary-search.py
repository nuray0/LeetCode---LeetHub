class Solution:
    def search(self, nums: List[int], target: int) -> int:

    
        start_index = 0
        end_index = len(nums)-1
        while start_index<=end_index:
            mid = (start_index+end_index)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start_index = mid+1
            elif nums[mid]>target:
                end_index = mid-1
        return -1
    
