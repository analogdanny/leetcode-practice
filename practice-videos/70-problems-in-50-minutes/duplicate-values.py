# Given an integer array `nums`, return true if any value appears 
# at least twice in the array, and return false if every element 
# is distinct.

class Solution:
    def containsDeplicate(self, nums: list[int]) -> bool:
        # A set cannot contain duplicates, therefore good for checking for duplicates
        # A set if implemented as a hash table and is fast.
        # - Lookup/insert/delete in a set is O(1)
        # - Unordered, immutable (unchangable), heterogeneous (data of all types), and 
        #   unique (no duplicates)
        # - Empty sets cannoy be created through {}, it creates a dictionary, unless
        #   you include values.
        #   - Since the value of a dict is a key, {1,2,3} is just unique values 
        
        # convert list to set
        nums_set = set(nums)
        
        if len(nums_set) == len(nums):
            return False
        else:
            return True
        
solve = Solution()

example1 = [1,2,3,1]
example2 = [1,2,3,4]
example3 = [1,1,1,3,3,4,3,2,4,2]

print(solve.containsDeplicate(example1))
print(solve.containsDeplicate(example2))
print(solve.containsDeplicate(example3))
