from typing import List
from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find median of two sorted arrays using binary search approach.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            
        Returns:
            Median value as float
        """
        # Ensure nums1 is the shorter array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Binary search on shorter array
            partition_x = (left + right) // 2
            partition_y = (m + n + 1) // 2 - partition_x
            
            # Get left and right elements for both arrays
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            # Check if we found the correct partition
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # If total length is odd
                if (m + n) % 2:
                    return max(max_left_x, max_left_y)
                # If total length is even
                return (max(max_left_x, max_left_y) + 
                       min(min_right_x, min_right_y)) / 2
            
            # Adjust binary search pointers
            elif max_left_x > min_right_y:
                right = partition_x - 1
            else:
                left = partition_x + 1
                
        raise ValueError("Input arrays are not sorted")



if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]

    print(Solution().findMedianSortedArrays(nums1, nums2))
