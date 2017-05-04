#!/usr/bin/env python


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result = result + min(nums[i], nums[i + 1])
        return result

if __name__ == "__main__":
    print(Solution().arrayPairSum([1, 4, 3, 2]))
