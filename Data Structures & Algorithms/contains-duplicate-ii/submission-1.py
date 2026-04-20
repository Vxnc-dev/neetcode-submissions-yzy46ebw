class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                if abs(l - r) <= k:
                    return True
                r += 1
                l = r - 1
            else:
                if r == len(nums)-1:
                    l += 1
                    r = l + 1
                else:
                    r += 1
        return False