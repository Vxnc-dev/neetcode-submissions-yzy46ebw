class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for detail in details:
            if detail[11:13].isnumeric() and int(detail[11:13]) > 60:
                counter+= 1
        
        return counter
                