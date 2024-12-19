#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/12/18 20:05
# @Author : limber
# @desc :
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # if len(nums) >= 2:
        #     s_point = 0
        #     min_length = 0
        #     while s_point <= len(nums) - 1:
        #         for f_point in range(s_point + 1, len(nums) + 1):
        #             total_ = 0
        #             section_list = nums[s_point:f_point]
        #             for value_ in section_list:
        #                 total_ += value_
        #             if total_ >= target and ((min_length == 0) or (len(section_list) < min_length)):
        #                 min_length = len(section_list)
        #                 break
        #             else:
        #                 f_point += 1
        #         s_point += 1
        #     return min_length
        #
        # else:
        #     if nums[0] >= target:
        #         return 1
        #     else:
        #         return 0

        # 滑动窗口
        l = len(nums)
        left = 0
        right = 0
        min_len = float("inf")
        cur_sum = 0
        while right < l:
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(float("inf"), right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1
        return min_len if min_len != float("inf") else 0


if __name__ == '__main__':
    result = Solution().minSubArrayLen(8, [1, 4, 4])
    print(result)
    # for i in range(1, 10):
    #     print(i)
