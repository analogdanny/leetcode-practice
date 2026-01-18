# Given an `m x n` matrix, return all elements of the matrix in spiral order.

class Solution():
    # # First attempt
    # def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
    #     dir = ["right", "down", "left", "up"]
        
    #     cur_dir = dir[0]
        
    #     row = 0
    #     col = 0

    #     res = []
        
    #     while (matrix):

    #         res.append(matrix[col][row])

    #         prev_dir = cur_dir
            
    #         # cut matrix ends
    #         if prev_dir == "right" and row == (len(matrix[0]) - 1):
    #             cur_dir = "down"
    #             matrix = matrix[1:]
    #         elif prev_dir == "down" and col == len(matrix) - 1:
    #             cur_dir = "left"
    #             matrix = [arr[:len(arr) - 1] for arr in matrix]
    #             row -= 1
    #         elif prev_dir == "left" and row == 0:
    #             cur_dir = "up"
    #             matrix = matrix[:len(matrix) - 1]
    #             col -= 1
    #         elif prev_dir == "up" and col == 0:
    #             cur_dir = "right"
    #             matrix = [arr[1:] for arr in matrix]
    #         else:
    #             if cur_dir == "right":
    #                 row += 1
    #             elif cur_dir == "down":
    #                 col += 1
    #             elif cur_dir == "left":
    #                 row -= 1
    #             elif cur_dir == "up":
    #                 col -= 1
            
    #     return res
    
    # Optimal Solution
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ret = []

        while matrix:
            # add first row/list of matrix to the list
            ret += matrix.pop(0)
            
            # append the last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    last_element = row.pop()  # pops off the last item in the row
                    ret.append(last_element)

            # add reverse of last row/list
            if matrix:
                last_row = matrix.pop() # pop off the last row of matrix
                # last_row[:-1] # last item in row            
                # last_row[::-1] # rever the row entirely
                ret += last_row[::-1]

            # append first element of all rows/lists in reverse
            if matrix and matrix[0]:

                # iterate rows in reverse
                for row in matrix[::-1]:
                    # pop the first item to get the left items
                    ret.append(row.pop(0))

        return ret
                    
        
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
       
solve = Solution()

print(solve.spiralOrder(matrix1))
print(solve.spiralOrder(matrix2))
