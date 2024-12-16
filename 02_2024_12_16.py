#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/16 21:41
# @Author : limber
# @desc :

"""
leetcode: 27
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 注意: 是原地移除

        # 解法1:
        # index_ = 0
        # while index_ != len(nums):
        #     if nums[index_] == val:
        #         del nums[index_]
        #     else:
        #         index_ += 1
        # return len(nums)

        # 解法2: 双指针解法
        slow_pointer = 0
        fast_pointer = 0
        while fast_pointer < len(nums):
            if nums[fast_pointer] != val:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
            fast_pointer += 1
        return len(nums[:slow_pointer])


if __name__ == '__main__':
    result = Solution().removeElement([3, 2, 2, 3], 3)
    print(result)

    # list1 = [1, 2, 3, 4, 5]
    # del list1[2]
    # print(len(list1))
    # print(list1)
