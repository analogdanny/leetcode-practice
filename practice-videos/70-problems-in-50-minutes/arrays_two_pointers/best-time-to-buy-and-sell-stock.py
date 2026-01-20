# You are given an array `prices` where `prices[i]` is the price of a given
# stock on the `ith` day.
#
# You want to maximize your profit by choosing a **single day** to buy one
# stock and choosing a **different day in the future** to sell that stock. 
#
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#

# Approach (Failed to solve how I wanted):
# - Greedy Algorithm: A type of optimization algorithm that makes locally 
#   optimal choices at each step to find a globally optimal solution.
#   - Operates on the principle of "taking the best option now" without
#     consideration of long-term consequences.


class Solution:
    # def maxProfit(self, prices: list[int]) -> int:

    #     # Use two pointers where we compare the value and iterate on if the value 
    #     # of L < R. We have to iterate all points. For each L, iterate R across and 
    #     # calculate all points.

    #     max_profit = 0 
        
    #     for i, left in enumerate(prices):
    #         for right in prices[i + 1:]:
    #             if right - left > max_profit:
    #                 max_profit = right - left
            
    #     return max_profit

    # Optimal Solution
    # O(N) time with left and right pointers moving through a single iteration
    # O(1) space with 3 variables
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        
        # len() will be +1 the index so once the right is out of scope,
        # all comparisons that matter will have been computed
        while right != len(prices):
            # only check if the left value is smaller than right value
            # otherwise, no max profit - no need to compute
            if prices[left] < prices[right]: 
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                # this is the greedy piece, if left is greater just set left to right
                # and skip computing others, looking for a better opportunity
                left = right
                
            right += 1
        
        return max_profit
            
prices1 = [7,1,5,3,6,4] # output 5
prices2 = [7,6,4,3,1]   # output 0

solve = Solution()
print(solve.maxProfit(prices1))
print(solve.maxProfit(prices2))
