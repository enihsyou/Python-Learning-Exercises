# -*- coding: utf-8 -*-
"""
File name: 1 Two Sum
Reference:
Introduction:
Date: 2016-10-12
Author: enihsyou
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                if a + b == target:
                    return [i, j + i + 1]
