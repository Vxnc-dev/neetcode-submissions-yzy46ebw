class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        res = []
        p = 0
        s += " "
        while p < len(s):
            if s[p] == " ":
                if count > 0:
                    res.append(count)
                count = 0
                p += 1
            else:
                count += 1
                p += 1
        return res[-1]