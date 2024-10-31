class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to zigzag pattern and return row-by-row reading.
        
        Args:
            s: Input string
            numRows: Number of rows in zigzag pattern
            
        Returns:
            String read row by row from zigzag pattern
        """
        # Handle special cases
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Initialize rows
        rows = [''] * numRows
        current_row = 0
        step = 1
        
        # Distribute characters to rows
        for char in s:
            # Add current character to its row
            rows[current_row] += char
            
            # Change direction at boundaries
            if current_row == 0:
                step = 1  # Going down
            elif current_row == numRows - 1:
                step = -1  # Going up
                
            # Move to next row
            current_row += step
        
        # Combine all rows
        return ''.join(rows)


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 4))