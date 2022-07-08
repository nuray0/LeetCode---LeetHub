class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq = [n*n for n in nums]
        sq_sorted = sorted(sq)
        return(sq_sorted)