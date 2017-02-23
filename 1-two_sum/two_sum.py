#!/usr/bin/env python

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for idx, num in enumerate(nums):
            next_idx = idx + 1
            
            while next_idx < len(nums):
                if nums[idx] + nums[next_idx] == target:
                    return [idx, next_idx]
                next_idx += 1

        return []

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))








