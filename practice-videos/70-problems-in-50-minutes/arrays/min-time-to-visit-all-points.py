# On a 2D plan, there are n points with integer coordinates `points[i] = [xi, yi]`.
# Return the minimum time in seconds to visit all the points in the order given
# by `points`.
#
# You can move according to these rules:
# - In 1 second, you can either:
#   - move vertically by one unit,
#   - move horizontally by one unit
#   - move diagonally `sqrt(2)` units (in other words, move one unit vertically then 
#     one unit horizontally in 1 second from x^2 + y^2 = z^2)
# - You have to visit the points in the same order as they appear in the array.
# - You are allowed to pass through points that appear later in the order, but these
#   do not count as visits



class Solution:
    # My attempt
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        # Store tuples as keys in set
        sec = 0
        visited = []
        
        cur_point = points[0]
        cur_point_x = cur_point[0]
        cur_point_y = cur_point[1]

        visited.append(cur_point)
        
        for i, target_point in enumerate(points[1:]):
            target_point_x = target_point[0]
            target_point_y = target_point[1]
        
            while cur_point != target_point:
                diff_x = abs(target_point_x - cur_point_x)
                diff_y = abs(target_point_y - cur_point_y)
                
                # Figure out the direction for movement
                inc_x = 1 if target_point_x > cur_point_x else -1
                inc_y = 1 if target_point_y > cur_point_y else -1
                
                # Check for diagonal movement
                if diff_x > 0 and diff_y > 0:
                    cur_point_x += inc_x
                    cur_point_y += inc_y
                # Check for vertical movement
                elif diff_y > 0:
                    cur_point_y += inc_y
                # Check for horizontal movement
                elif diff_x > 0:
                    cur_point_x += inc_x
                
                cur_point = [cur_point_x, cur_point_y]

                if cur_point not in visited:
                    sec += 1
                    visited.append(cur_point)

        return sec
            
    # Optimal solution: O(n)
    def minTimeToVisitAllPoints(self, points: list[int, int]) -> int:
        seconds = 0
        # you can pop values off a list like a stack
        x1, y1 = points.pop()
        
        # loop until points is empty
        while(points):
            x2, y2 = points.pop()
            # This works because regardless of moving diagonal, 1x X or 1x Y you're using 
            # 1 second. Therefore, its about whichever absolute difference is the larger 
            # to determine seconds.
            seconds += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2 # update the current coordinates.
        
        return seconds
        
points1 = [[1,1],[3,4],[-1,0]]

solve = Solution()

print(solve.minTimeToVisitAllPoints(points1))