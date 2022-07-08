
class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = {}
        for n in nums:
            if n in uniques:
                uniques[n] += 1
            else:
                uniques[n] = 1
        
        for key in uniques:
            if uniques[key] > 1:
                return True
        return False
    
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        uniques = set(nums)
#        if len(uniques) != len(nums):
#            return True
#        return False

    
    
   
    
 