class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
            else:
                index_delete = t.index(i)
                t = t[:index_delete] + t[index_delete + 1:]
        if len(t) == 0:
            return True
        return False