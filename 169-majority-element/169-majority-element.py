class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = -1
        max_digit = -1
        d = collections.Counter(nums)
        for i in d:
            if d[i] > majority:
                majority = d[i]
                max_digit = i

        return max_digit