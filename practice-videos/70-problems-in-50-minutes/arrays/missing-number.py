# Given an array `nums` containing `n` distinct numbers in the range [0, n], return the only 
# number in the range that is missing from the array.

class Solution:
    # def missingNumber(self, nums: list[int]) -> int:
    #     # My attempt: n log(n) due to sort
        
    #     # sort the list
    #     n = len(nums)
    #     if n not in nums:
    #         return n
        
    #     sorted_list = nums
    #     sorted_list.sort()  # n log(n)
          
          # Linear
    #     for i, num in enumerate(sorted_list):
    #         if i != num:
    #             return i            
    
    
    # Optimal answer: Take the expected sum of the list and subtract the 
    #                 actual sum of the list, yielding the difference and 
    #                 missing number.
    def missingNumber(self, nums: list[int]) -> int:
        # range increments from 0 -> n - 1 and excludes the last value, 
        # need to add 1 to the length so range goes from 0 -> n
        expected_sum = range(len(nums) + 1)
        difference_sums = sum(expected_sum) - sum(nums)
        return difference_sums
        
        
solve = Solution()
 
example1 = [3,0,1]              # output = 2
example3 = [0,1]                # output = 2
example2 = [9,6,4,2,3,5,7,0,1]  # output = 8

print(solve.missingNumber(example1))     
print(solve.missingNumber(example3))     
print(solve.missingNumber(example2))