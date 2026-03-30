class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)
        count_s2 = Counter()
        l = 0
        for r in range(len(s2)):
            char_r = s2[r]
            count_s2[char_r] += 1
            
            if r - l + 1 > len(s1):
                char_l = s2[l]
                count_s2[char_l] -= 1
                if count_s2[char_l] == 0:
                    del count_s2[char_l]
                l += 1
            
            if count_s1 == count_s2:
                return True
        return False