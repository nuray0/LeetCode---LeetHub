# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
    
        r = n-1
        l = 0
        while(l<=r):
            mid = int((l+r)/2)
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l
    

        