class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        s.sort()
        prefix = s[0]

        while not s[-1].startswith(prefix):
            prefix = prefix[:-1]

        return prefix