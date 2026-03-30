class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ele = nums1 + nums2
        ele.sort()
        if not ele:
            return 0
        if len(ele) % 2 == 0:
            i = ele[(len(ele) // 2) - 1]
            j = ele[(len(ele) // 2)]
            return (j+i) /2
        else:
            return ele[len(ele) // 2]