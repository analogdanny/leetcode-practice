# This problem requires knowledge of two algorithms
# 
# Breath-First Search
#   Traverse through one level of children nodes, then traverse through 
#   the level of grandchildren nodes (and so on...)
# 
#                   1
#                 /   \
#               2       3
#              / \     / \
#             4   5   6   7
# 
# Depth-First Search (DFS) 
#   Traverse through the left subtree(s) first, then traverse through the right
#   subtree(s).
#
#                   1
#                 /   \
#               2       5
#              / \     / \
#             3   4   6   7
#
# Problem: Given a 2D m*n grid, where 1 is land and 0 is water, return the
#          number of islands in the grid.
#
#          Example: [
#           "1", "1", "1", "1", "0" 
#           "1", "1", "0", "1", "0"            =>   1 Island
#           "1", "1", "0", "0", "0" 
#           "0", "0", "0", "0", "0" 
#          ]

# To use a queue/deque we need to import from collections
#
# Dequeues in python are double ended queues by default
# - Can queue/dequeue an element from both sides of the queue.
# - Functions are .appendleft(), .append(), .popleft(), .pop()
from collections import deque

# This solution is time complexity of O(m*n)
# Actual time complexity is O(4*m*n) but when it grows so large for m and n
# the 4 becomes insignificant and gets dropped.
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
              
        if not grid:
            return 0
        
        # need a BFS algorithm
        def bfs(r: str,c: str) -> None:
            # create the deque
            queue = deque()
            
            # add the set of coordinates to the visited set
            visited.add((r,c))
            
            # then append this coordinate to the queue
            queue.append((r,c))
            
            # while the queue has items, we iterate through the neighbors until
            # there are none left
            while queue:
                # let's pop the queues first coordinate
                row, col = queue.popleft()
                
                # additionally, we assign all directions for potential neighbors
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                # check all directions
                for dir_r, dir_c in directions:
                    # assign the r and c values to  the row/col popped + direction
                    r, c = row + dir_r, col + dir_c  
                    
                    # if the grid value is 1 and not in visited and in range of m*n
                    if ( r in range(rows) and
                         c in range(cols) and
                         grid[r][c] == '1' and
                         (r, c) not in visited
                    ):
                        # append to queue and visited
                        queue.append((r,c))
                        visited.add((r,c))
        
        # need a counter for islands, rows and cols tracker, and visited indices tracker
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        # iterate over the range of rows
        # Note: the length is +1 and range is -1, so no index correction needed here
        for r in range(rows):
            # iterate over the cols
            for c in range(cols):
                # check if the value of the grid is "1" and that we have not visited yet
                if grid[r][c] == '1' and (r,c) not in visited:
                    # call the BFS algorithm here (find all neighbors?)
                    # - it will add in all the visited nodes so we don't consider those neighbors
                    #   again as individual islands.
                    bfs(r,c)
                    count += 1
        
        return count
    
grid1 = [
    ["1", "1", "1", "1", "0"], 
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"], 
    ["0", "0", "0", "0", "0"], 
]

grid2 = [
    ["1", "1", "1", "1", "0"], 
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"], 
    ["0", "0", "0", "0", "1"], 
]

solve = Solution()
print(solve.numIslands(grid1))
print(solve.numIslands(grid2))
