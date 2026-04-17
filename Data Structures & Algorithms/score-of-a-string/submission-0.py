class Solution:
    def scoreOfString(self, s: str) -> int:
        score_values = {
        "a": 97, "i": 105, "q": 113, "y": 121,
        "b": 98, "j": 106, "r": 114, "z": 122,
        "c": 99, "k": 107, "s": 115,
        "d": 100, "l": 108, "t": 116,
        "e": 101, "m": 109, "u": 117,
        "f": 102, "n": 110, "v": 118,
        "g": 103, "o": 111, "w": 119,
        "h": 104, "p": 112, "x": 120,
        }
        score = 0
        l, r = 0, 1
        while r < len(s):
            diff = score_values[s[r]] - score_values[s[l]]
            if diff < 0:
                diff *= -1
            score = score + diff
            l += 1
            r += 1
        return score
