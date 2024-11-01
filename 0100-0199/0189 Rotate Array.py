from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate array to the right by k steps in-place.
        
        Args:
            nums: Array to rotate
            k: Number of positions to rotate right
            
        Returns:
            None (modifies nums in-place)
        """
        def reverse(start: int, end: int) -> None:
            """Helper function to reverse array segment."""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        # Handle edge cases
        if n <= 1:
            return
            
        # Normalize k to prevent unnecessary rotations
        k = k % n
        if k == 0:
            return
            
        # Reverse entire array, then reverse parts
        reverse(0, n - 1)      # Reverse whole array
        reverse(0, k - 1)      # Reverse first k elements
        reverse(k, n - 1)      # Reverse remaining elements


if __name__ == "__main__":
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))

