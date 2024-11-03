from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determine if you can complete a circuit starting from any gas station.
        Args:
            gas: List of gas station gas amounts
            cost: List of gas station costs
            
        Returns:
            Index of starting gas station if solution exists, -1 otherwise
        """ 
        # If total gas is less than total cost, no solution exists
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # If we can't get to i+1, we need to start over from i+1
                # We can skip all stations between start and i because they
                # would have even less gas
                start = i + 1
                tank = 0
        
        return start


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))
