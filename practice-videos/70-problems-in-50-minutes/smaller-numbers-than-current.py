# Given the array `nums`, for each `nums[i]` find out how many numbers in the
# array are smaller than it. That is, for each `nums[i]` you have to count the 
# number of valid `j's` such that `j != i` and `nums[j] < nums[i]``

class Solution:
    def smallNumbersThanCurrent(self, nums: list) -> list:
        
        # Sort the array and then small numbers will be its index - 1
        sorted_nums = sorted(nums)
        
        # the index() call is O(n) so its worse time complexity of O(n^2)?
        # ret = [sorted_nums.index(num) for num in nums]
        
        # so instead, we can use a hashmap
        sorted_nums_map = {}
        
        for i, n in enumerate(sorted_nums):
            if n not in sorted_nums_map:
                sorted_nums_map[n] = i

        ret = []

        for i in nums:
            ret.append(sorted_nums_map[i])
            
        return ret

nums1 = [8,1,2,2,3]   # output [4,0,1,1,3]
nums2 = [6,5,4,8]     # output [2,1,0,3]
nums3 = [7,7,7,7]     # output [0,0,0,0]

solve = Solution()

print(solve.smallNumbersThanCurrent(nums1))
print(solve.smallNumbersThanCurrent(nums2))
print(solve.smallNumbersThanCurrent(nums3))
