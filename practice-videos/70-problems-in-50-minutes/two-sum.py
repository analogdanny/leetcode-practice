# Given an array of integers `nums` and an integer `target`, 
# return indices of the two numbers such that they add up to `target`

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # My first attempt
        # for i, num in enumerate(nums):
        #     two_sum_value = target - num
        #     if two_sum_value in nums:
        #         # list.index() is a linear scan O(n)
        #         two_sum_index = nums.index(two_sum_value)
        #         if i != two_sum_index:
        #             return [i, two_sum_index]
        
        # Can use a hashmap, constant time O(1)
        index_map = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            # lookup in hashmap is also O(1)
            # return the two indices if found in map
            if diff in index_map:
                return [i, index_map[diff]]
            
            # otherwise, we store the current value and its index
            index_map[num] = i

        
nums1, target1 = [2,7,11,15], 9  # output = [0,1] 
nums2, target2 = [3,2,4], 6      # output = [1,2]
nums3, target3 = [3,3], 6        # output = [0,1]

solve = Solution()
print(solve.twoSum(nums1, target1))
print(solve.twoSum(nums2, target2))
print(solve.twoSum(nums3, target3))
