from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Distribute candies to children based on their ratings.
        Rules:
        1. Each child must have at least one candy
        2. Children with higher ratings get more candies than their neighbors
        
        Args:
            ratings: List of children's ratings
        Returns:
            Minimum total number of candies needed
        """
        children = len(ratings)
        # Initialize each child with 1 candy
        candy_array = [1 for _ in range(children)]

        # Forward pass: compare with left neighbor
        # Ensure each child with a higher rating than their left neighbor
        # gets more candies than that neighbor
        for i in range(1, children):
            if ratings[i] > ratings[i - 1]:
                candy_array[i] = candy_array[i - 1] + 1

        # Backward pass: compare with right neighbor
        # If rating is higher than right neighbor but candies are not,
        # increase candies to be one more than right neighbor
        for i in range(children - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candy_array[i] <= candy_array[i + 1]:
                candy_array[i] = candy_array[i + 1] + 1

        return sum(candy_array)


if __name__ == "__main__":
    print(Solution().candy([1, 0, 2]))
    print(Solution().candy([1, 2, 2]))
