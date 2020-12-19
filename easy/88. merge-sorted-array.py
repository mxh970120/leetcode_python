'''
Author: mxh970120
Date: 2020.12.19
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 有序数组，可以双指针
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        # 如果此时nums2还没读完
        nums1[:n] = nums2[:n]
        return nums1



if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solu = Solution()
    print(solu.merge(nums1, m, nums2, n))