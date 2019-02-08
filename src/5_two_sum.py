"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len0 = len(nums)
        #len_sum = len0 * (len0 - 1) / 2
        sum_dic = {}
        for i in range(0, len0 - 1):
            for j in range(i+1, len0):
                tmp = nums[i] + nums[j]
                sum_dic[tmp] = [i, j]
        #print(sum_dic)
        for sum_each in sum_dic.keys():
            if sum_each == target:
                print(sum_dic[sum_each])
                return sum_dic[sum_each]
            else:
                continue


my1 = Solution()
my1.twoSum([2, 7, 11, 15], 9)






