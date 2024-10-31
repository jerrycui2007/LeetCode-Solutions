from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        Find minimum total distance for robots to reach factories.
        
        Args:
            robot: List of robot positions
            factory: List of [factory_position, capacity] pairs
            
        Returns:
            Minimum total distance traveled by all robots
        """
        # Sort both robots and factories by position
        self.robot = robot
        self.robot.sort()
        self.factory = factory
        self.factory.sort()
        
        # Create cache for dynamic programming
        self.cache = {}
            
        return self.find_min_distance(0, 0, 0)

    def find_min_distance(self, robot_index: int, factory_index: int, spots_used: int) -> int:
            """Helper function to find minimum distance using recursion.
            
            Args:
                robot_index: Current robot's position in the list
                factory_index: Current factory's position in the list
                spots_used: Number of spots used in current factory
            """
            # Base cases
            if robot_index == len(self.robot):  # All robots assigned
                return 0
            if factory_index == len(self.factory):  # No more factories
                return float('inf')
            
            # Check if we've solved this case before
            state = (robot_index, factory_index, spots_used)
            if state in self.cache:
                return self.cache[state]
            
            # Try skipping current factory
            min_distance = self.find_min_distance(robot_index, factory_index + 1, 0)
            
            # Try using current factory if spots are available
            if spots_used < self.factory[factory_index][1]:
                distance = abs(self.robot[robot_index] - self.factory[factory_index][0])
                next_distance = self.find_min_distance(robot_index + 1, factory_index, spots_used + 1)
                if next_distance != float('inf'):
                    min_distance = min(min_distance, distance + next_distance)
            
            # Save result in cache
            self.cache[state] = min_distance
            return min_distance


if __name__ == "__main__":
    print(Solution().minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]]))
        