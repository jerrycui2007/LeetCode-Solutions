from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val in nums in-place.
        
        Args:
            nums: Input array of integers
            val: Value to remove
            
        Returns:
            k: Number of elements not equal to val
        """
        # Handle empty array
        if not nums:
            return 0
            
        # Use two-pointer technique
        write_pos = 0  # Position to write next valid element
        
        # Iterate through array
        for read_pos in range(len(nums)):
            # If current element is not val, keep it
            if nums[read_pos] != val:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos


if __name__ == "__main__":
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))