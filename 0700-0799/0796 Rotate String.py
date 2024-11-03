class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False


if __name__ == "__main__":
    print(Solution().rotateString("abcde", "cdeab"))
    print(Solution().rotateString("abcde", "abced"))
