from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mn = m + n
        odd = mn % 2
        med = mn // 2
        i_m = 0
        i_n = 0
        counter = 0

        median = []

        while i_m < m and i_n < n:
            if nums1[i_m] > nums2[i_n]:
                num = nums2[i_n]
                i_n += 1
            else:
                num = nums1[i_m]
                i_m += 1

            if not odd:
                if counter == med - 1:
                    median.append(num)

            if counter == med:
                median.append(num)
                return sum(median) / len(median)

            counter += 1

        while i_m < m:
            num = nums1[i_m]
            i_m += 1

            if not odd:
                if counter == med - 1:
                    median.append(num)

            if counter == med:
                median.append(num)
                return sum(median) / len(median)

            counter += 1

        while i_n < n:
            num = nums2[i_n]
            i_n += 1

            if not odd:
                if counter == med - 1:
                    median.append(num)

            if counter == med:
                median.append(num)
                return sum(median) / len(median)

            counter += 1


if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
    ]
    test_results = [
        2.0,
        2.5,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.findMedianSortedArrays(test[0], test[1]) == result

    print("Passed")
