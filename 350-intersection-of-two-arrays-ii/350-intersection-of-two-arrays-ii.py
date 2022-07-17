class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        p1 = p2 = 0
        nums1, nums2 = sorted(nums1), sorted(nums2)

        while (p1 < len(nums1) and p2 < len(nums2)):
            if nums1[p1] > nums2[p2]:
                p2 += 1

            elif nums1[p1] < nums2[p2]:
                p1 += 1

            else:
                output.append(nums1[p1])
                p1 += 1
                p2 += 1
            
        return output
    
    
        # dictionary to count
        # almost the same runtime and memory usage as pointers
#        output = []
#        counts = {}
#
#        for num in nums1:
#            counts[num] = counts.get(num, 0) + 1
#
#        for num in nums2:
#            if num in counts and counts[num] > 0:
#                output.append(num)
#                counts[num] -= 1
#
#        return output


        # same as dictionary, but using counter
#        output = []
#        counts = collections.Counter(nums1)
#        
#        for num in nums2:
#            if num in counts and counts[num] > 0:
#                output += num,
#                counts[num] -= 1
#                
#        return output

    
        # bruteforce solution
#        output = {}
#        for i in range(len(nums1)):
#            for j in range(len(nums2)):
#                if nums2[j] == nums1[i] and j not in output:
#                    output[j] = nums2[j]
#                    break
#        return output.values()
    
    

        