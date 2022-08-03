class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []
        out = {}
        
        d = {}
        for i in range(length):
            d[nums[i]] = i
    
        for i in range(length):
            for j in range(i + 1, length):
                target = - nums[i] - nums[j]
                if target in d and d[target] != i and d[target] != j:
                    to_append = tuple(sorted((nums[i], nums[j], target)))
                    if not to_append in out:
                        out[to_append] = 0
                    
        return out