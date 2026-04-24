class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            add = 0
            if op == "+":
                record.append(int(record[-1] + record[-2]))
            elif op == "C":
                record.pop()
            elif op == "D":
                add = 2 * record[-1]
                record.append(int(add))
            else:
                record.append(int(op))
        res = 0
        for i in record:
            res += i
        return res