class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = list(set(nums))
        for num in s:
            nums.remove(num)
        for num in nums:
            s.remove(num)
        return s[0]
        