# Given an integer array `nums` sorted in non-decreasing order, return
# an array of the squares of each number sorted in non-decreasing order.
#
# Follow up: squaring each element and sorting the new array is very trivial, 
# find an O(n) solution using a different approach

from collections import deque

class Solution:
    # My solution - O(n^2)
    # def sortedSquares(self, nums: list[int]) -> list[int]:
    #     sorted_squares = []
        
    #     for num in nums:
    #         squared = num**2
            
    #         if len(sorted_squares) == 0 or squared > sorted_squares[0]:
    #             sorted_squares.append(squared)
    #         elif squared < sorted_squares[0]:
    #             sorted_squares.insert(0, squared)

    #     return sorted_squares

    # # Easiest O(n log(n))
    # def sortedSquares(self, nums: list[int]) -> list[int]:
    #     sorted_squares = [num**2 for num in nums]
    #     sorted_squares.sort()
    #     return sorted_squares

    # # Split and merge solution O(n)
    # # 1. Find index 0 (loop O(n))
    # # 2. Reverse negatives up to 0 (O(N))
    # # 3. Square and merge (O(n))
    # def sortedSquares(self, nums: list[int]) -> list[int]:
    #     if not nums:
    #         return nums
        
    #     if nums[0] > 0:
    #         return [nums**2 for num in nums]
        
    #     # find the first index
    #     index0 = 0
    #     for i, num in enumerate(nums):
    #         # find first number >= 0
    #         # if not found the nums should be ordered
    #         if num >= index0:
    #             index0 = i 
    #             break
        
    #     positive_nums = nums[index0:]
    #     # example, [-4, -1] -> [1, 16]
    #     reversed_negatives = [-1*num for num in reversed(nums[:index0])]
        
    #     # merge
    #     a = b = 0
    #     ret = []
        
    #     while a < len(positive_nums) and b < len(reversed_negatives):
            
    #         if positive_nums[a] < reversed_negatives[b]:
    #             ret.append(positive_nums[a])
    #             a += 1
            
    #         else:
    #             ret.append(reversed_negatives[b])
    #             b += 1
                
    #     if a < len(positive_nums):
    #         ret.extend(positive_nums[a:])
    #     else:
    #         # ret.extend(reversed_negatives[b:])
    #         ret += reversed_negatives[b:]

    #     return [n**2 for n in ret]
    
    # Optimal Solution: Absolute and Merge
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sorted_squares = deque()
        left = 0
        right = len(nums) - 1

        while left <= right:
            left_val, right_val = abs(nums[left]), abs(nums[right])
            
            if left_val > right_val:
                sorted_squares.appendleft(left_val**2)
                left += 1
            else:
                sorted_squares.appendleft(right_val**2)
                right -= 1
        
        return list(sorted_squares)

    
solve = Solution()

example1 = [-4, -1, 0, 3, 10]
example2 = [-7, -3, 2, 3, 11]

print(solve.sortedSquares(example1))
print(solve.sortedSquares(example2))
