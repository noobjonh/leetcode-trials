class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Find the median of the combined sorted arrays.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        
        n = len(nums)
        
        if n % 2 == 1:  
            median_index = n // 2
            return float(nums[median_index])
        else: 
            median_index = n // 2
            median_value = (nums[median_index - 1] + nums[median_index]) / 2.0
            return median_value