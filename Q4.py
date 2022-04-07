class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sum=(nums1+nums2)

        sum.sort()

        if len(sum) %2:
            return sum[int((len(sum)-1)/2)]
        else:
            return (sum[int(len(sum)/2)]+sum[int(len(sum)/2-1)])/2
