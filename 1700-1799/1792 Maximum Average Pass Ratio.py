from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Define a function to calculate the marginal gain
        def marginalGain(pass_students, total_students):
            return (pass_students + 1) / (total_students + 1) - pass_students / total_students

        # Create a max-heap based on marginal gain
        heap = []
        for pass_students, total_students in classes:
            heapq.heappush(heap, (-marginalGain(pass_students, total_students), pass_students, total_students))

        # Distribute extra students
        for _ in range(extraStudents):
            gain, pass_students, total_students = heapq.heappop(heap)
            pass_students += 1
            total_students += 1
            heapq.heappush(heap, (-marginalGain(pass_students, total_students), pass_students, total_students))

        # Calculate the new average pass ratio
        total_average = 0
        for _, pass_students, total_students in heap:
            total_average += pass_students / total_students

        return total_average / len(classes)


if __name__ == "__main__":
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4

    solution = Solution().maxAverageRatio(classes, extraStudents)
    print(solution)


