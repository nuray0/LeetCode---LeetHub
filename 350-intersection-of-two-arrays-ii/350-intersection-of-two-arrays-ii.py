class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i] and j not in output:
                    output[j] = nums2[j]
                    break
                else: continue
        return output.values()
        