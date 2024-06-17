"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i
        
        for i in range(n):
            cont = target - nums[i]
            if cont in numMap and numMap[cont] != i:
                return numMap[cont], i
