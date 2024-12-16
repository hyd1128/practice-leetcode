#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/10 23:42
# @Author : limber
# @desc :

"""
leetcode: 704
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法
        # 左闭右闭区间
        left_, right_ = 0, len(nums) - 1
        while left_ <= right_:
            middle_ = left_ + (right_ - left_) // 2
            if nums[middle_] > target:
                right_ = middle_ - 1
            elif nums[middle_] < target:
                left_ = middle_ + 1
            else:
                return middle_

        return -1


if __name__ == '__main__':
    result = Solution().search([1, 2, 3, 4, 5], 2)
    print(result)
