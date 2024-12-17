#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/17 23:27
# @Author : limber
# @desc :

"""
leetcode: 977
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 解法1: 暴力破解
        # for index_ in range(len(nums)):
        #     nums[index_] = nums[index_] ** 2
        # nums.sort()
        # return nums

        # 解法2: 双指针破解
        result = [1] * len(nums)
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                result[i] = nums[r] ** 2
                r -= 1
            else:
                result[i] = nums[l] ** 2
                l += 1
            i -= 1
        return result


if __name__ == '__main__':
    result = Solution().sortedSquares([-4, -1, 0, 3, 10])
    print(result)
