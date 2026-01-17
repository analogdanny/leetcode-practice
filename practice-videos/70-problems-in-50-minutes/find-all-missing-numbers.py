# Given an array `nums` of `n` integers where `nums[i]` is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appears in nums

class Solution:
    # # My attempt, good O(n) solution
    # def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    #     n = len(nums)        
        
    #     missing_numbers = []
    #     # Unordered set -> O(1)
    #     seen = set(nums)
        
    #     # O(n) if completed
    #     for i in range(1, n + 1):
    #         # Check if i is in set, else append as missing
    #         # if i in seen:
    #         #     continue
    #         # missing_numbers.append(i)
            
    #         if i not in seen:
    #             missing_numbers.append(i)
            
    #     return missing_numbers
        
    # Optimal O(1) Solution
    # Key idea:
    # Use the input array itself as a marker to record which numbers have been seen.
    # This avoids extra space and achieves O(1) auxiliary space.
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        # First pass: mark seen numbers
        for i in range(len(nums)):
            # nums[i] may already be negative from a previous marking,
            # so take abs() to recover the original value.
            #
            # Subtract 1 to convert the value range [1, n]
            # into valid index range [0, n-1].
            temp = abs(nums[i]) - 1

            # If the value at index `temp` is positive,
            # negate it to mark that (temp + 1) exists in the array.
            #
            # We only negate once to avoid flipping it back to positive.
            if nums[temp] > 0:
                nums[temp] *= -1

        # Second pass: collect missing numbers
        missing_numbers = []

        # Iterate through the modified array
        for i, num in enumerate(nums):
            # If nums[i] is still positive,
            # it means (i + 1) was never encountered in the first pass
            if num > 0:
                missing_numbers.append(i + 1)

        return missing_numbers
        
solve = Solution()

example1 = [4,3,2,7,8,2,3,1]    # n = 8, output = [5,6] 
example2 = [1,1]                # n = 2, output = [2] 

print(solve.findDisappearedNumbers(example1))
print(solve.findDisappearedNumbers(example2))
