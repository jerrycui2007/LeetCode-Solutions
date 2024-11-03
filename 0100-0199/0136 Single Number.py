from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the single number in an array where every other number appears twice.

        Args:
            nums: List of integers
        Returns:
            Single number
        """
        single_number = 0

        # Use XOR to find the single number
        # XOR of a number with itself is 0
        # XOR of a number with 0 is the number itself
        # Therefore after XORing all numbers, the result is the single number
        for num in nums:
            single_number ^= num

        return single_number


if __name__ == "__main__":
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
