class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, len(nums1)-1
        idx = 0
        while l < m:
            l += 1
        
        for i in range(l, r+1):
            nums1[i] = nums2[idx]
            idx += 1
        
        nums1.sort()