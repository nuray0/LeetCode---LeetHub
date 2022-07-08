
class Solution:
    
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)
        if len(uniques) != len(nums):
            return True
        return False

    
    
   
    
 