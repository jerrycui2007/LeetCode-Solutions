from random import randint
from typing import List, Dict

class RandomizedSet:
    def __init__(self):
        """
        Initialize data structures for constant time operations.
        """
        # List to store values for O(1) random access
        self.values: List[int] = []
        # Dictionary to store value -> index mapping for O(1) lookup
        self.value_to_index: Dict[int, int] = {}

        self.num_values = 0
        
    def insert(self, val: int) -> bool:
        """
        Insert value if not present.
        Time complexity: O(1)
        
        Args:
            val: Value to insert
            
        Returns:
            True if value was inserted, False if already exists
        """
        if val in self.value_to_index:
            return False
            
        # Add value to end of list and store its index
        self.value_to_index[val] = len(self.values)
        self.values.append(val)
        self.num_values += 1
        return True
        
    def remove(self, val: int) -> bool:
        """
        Remove value if present.
        
        Args:
            val: Value to remove
            
        Returns:
            True if value was removed, False if not found
        """
        if val not in self.value_to_index:
            return False
            
        # Get index of value to remove
        index = self.value_to_index[val]
        last_val = self.values[-1]
        
        # Move last element to the removed element's position
        self.values[index] = last_val
        self.value_to_index[last_val] = index
        
        # Remove the last element
        self.values.pop()
        del self.value_to_index[val]

        self.num_values -= 1

        return True
        
    def getRandom(self) -> int:
        """
        Get random element.
        
        Returns:
            Random value from set
        """
        return self.values[randint(0, self.num_values - 1)]
