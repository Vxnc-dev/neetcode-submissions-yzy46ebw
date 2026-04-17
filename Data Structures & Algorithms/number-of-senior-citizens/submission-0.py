class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            l, r = 0, 1
            string = ""
            for i in d:
                if i == "M" or i == "F" or i == "O":
                    l += 1
                    r += 1
                    string = d[l] + d[r]
                    if int(string) > 60:
                        res += 1
                        break
                else:
                    l += 1
                    r += 1
        return res
                