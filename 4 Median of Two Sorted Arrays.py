from typing import List
from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_nums = len(nums1) + len(nums2)
        current = 0

        # Store original lengths before padding
        len1, len2 = len(nums1), len(nums2)

        # avoid IndexError by making arrays equal length
        while len(nums1) != len(nums2):
            if len(nums1) < len(nums2):
                nums1.append(inf)
            else:
                nums2.append(inf)

        if total_nums % 2 == 1:
            target_index = total_nums // 2
            counter1 = counter2 = 0

            while current != target_index:
                # Check if we've reached the end of original arrays
                if counter1 >= len1:
                    counter2 += 1
                elif counter2 >= len2:
                    counter1 += 1
                else:
                    if nums1[counter1] < nums2[counter2]:
                        counter1 += 1
                    else:
                        counter2 += 1
                current += 1

            # Check bounds when returning final value
            if counter1 >= len1:
                return nums2[counter2]
            elif counter2 >= len2:
                return nums1[counter1]
            return min(nums1[counter1], nums2[counter2])

        else:
            target_index = total_nums / 2 - 1

            counter1 = 0
            counter2 = 0

            while current != target_index:
                if nums1[counter1] < nums2[counter2]:
                    counter1 += 1
                else:
                    counter2 += 1

                current += 1

            if nums1[counter1] < nums2[counter2]:
                median = nums1[counter1]
                counter1 += 1
            else:
                median = nums2[counter2]
                counter2 += 1

            if nums1[counter1] < nums2[counter2]:
                median += nums1[counter1]
                counter1 += 1
            else:
                median += nums2[counter2]
                counter2 += 1

            return median / 2



if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]

    print(Solution().findMedianSortedArrays(nums1, nums2))
