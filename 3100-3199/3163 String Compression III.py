from typing import List


class Solution:
    def compressedString(self, word: str) -> str:
        """
        Helper function to compress a string using run-length encoding.
        Example: "aaa" -> "3a", "aaaaaaaaaaaaaabb" -> "14a2b"
        
        Args:
            word: String to compress
            
        Returns:
            Compressed string using run-length encoding
        """
        if not word:
            return ""
            
        comp = []
        counter = 1
        current_char = word[0]

        for char in word[1:]:
            if char == current_char:
                counter += 1
                # Handle groups of 9 characters
                if counter == 9:
                    comp.extend([str(counter), current_char])
                    counter = 0
            else:
                if counter:
                    comp.extend([str(counter), current_char])
                current_char = char
                counter = 1

        # Handle the last group
        if counter:
            comp.extend([str(counter), current_char])

        return "".join(comp)


if __name__ == "__main__":
    print(Solution().compressedString("aaaaaaaaaaaaaabb"))
    print(Solution().compressedString("aaa"))

