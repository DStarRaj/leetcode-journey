class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2 or not nums1:
            return
        i = 0
        j = 0
        m_index = m
        while i < (m + n) and j < n:
            if nums1[i] > nums2[j]:
                # Shifting
                for k in range(m_index, i, -1):
                    nums1[k] = nums1[k - 1]
                nums1[i] = nums2[j]
                m_index += 1
                j += 1
            i += 1

        while m_index < m + n:
            nums1[m_index] = nums2[j]
            m_index += 1
            j += 1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
        ([1, 2, 4, 5, 6, 0], 5, [3], 1),
    ]
    test_results = [
        [1, 2, 2, 3, 5, 6],
        [1],
        [1],
        [1, 2, 3, 4, 5, 6],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        a.merge(test[0], test[1], test[2], test[3])
        assert test[0] == result

    print("Passed")
