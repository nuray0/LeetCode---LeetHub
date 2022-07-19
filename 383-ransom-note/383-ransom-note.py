class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                index_delete = magazine.index(i)
                magazine = magazine[:index_delete] + magazine[index_delete + 1:]
        return True