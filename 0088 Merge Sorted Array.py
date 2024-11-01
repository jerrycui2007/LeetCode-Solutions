from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays in-place.
        
        Args:
            nums1: First sorted array with extra space at end
            m: Number of actual elements in nums1
            nums2: Second sorted array
            n: Number of elements in nums2
            
        Returns:
            None (modifies nums1 in-place)
        """
        # Handle edge cases
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2
            return
            
        # Start from the end of both arrays
        last_index = m + n - 1      # Last position in nums1
        nums1_index = m - 1         # Last actual element in nums1
        nums2_index = n - 1         # Last element in nums2
        
        # Merge arrays from right to left
        while nums1_index >= 0 and nums2_index >= 0:
            # Compare elements and place larger one at the end
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[last_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[last_index] = nums2[nums2_index]
                nums2_index -= 1
            last_index -= 1
        
        # If any elements remain in nums2, copy them to nums1
        # (no need to check nums1 as elements are already in place)
        while nums2_index >= 0:
            nums1[last_index] = nums2[nums2_index]
            nums2_index -= 1
            last_index -= 1


if __name__ == "__main__":
    print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

