class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(nums)-1
        e = len(nums)-1

        while l <= e:
            nums.insert(r+1, nums[l])
            r += 1
            l += 1
        return nums