class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    
        # method for manual comparison
#        for i in s:
#            if i not in t:
#                return False
#            else:
#                index_delete = t.index(i)
#                t = t[:index_delete] + t[index_delete + 1:]
#        if len(t) == 0:
#            return True
#        return False