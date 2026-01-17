//https://leetcode.com/problems/rotate-image/

/*
    Examples

     1. Given input matrix = 
        [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ],

        rotate the input matrix in-place such that it becomes:
        [
        [7,4,1],
        [8,5,2],
        [9,6,3]
        ]

    2.  Given input matrix =
        [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
        ], 

        rotate the input matrix in-place such that it becomes:
        [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
        ]
*/

#include <vector>
#include <array>
#include <utility>
#include <iostream>

#define solution 1

using namespace std;

class Solution {
public:

#if solution == 1 

    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        
        cout << n;
        cout << endl;
        cout << endl;

        for(int i = n, j = 0; i >= 2; i-=1, j+=1)
        {
            cout << i;
            cout << endl;
            cout << j;
            cout << endl;
            pair<int,int> top_left = { j, j };
            pair<int,int> top_right = { j, i-1 };
            pair<int,int> bottom_left = { i-1, j };
            pair<int,int> bottom_right = { i-1, i-1 };
            rotateFrame(matrix, top_left, top_right, bottom_left, bottom_right, n);
        }

    }

    void rotateFrame(vector<vector<int>>& matrix, pair<int,int> top_left, pair<int,int> top_right,
                                              pair<int,int> bottom_left, pair<int,int> bottom_right,
                                              int size)
    {   
        int tempArray[size];

        //save the top row
        for(int i = top_left.first; i < top_right.second; i++)
        {
            tempArray[i] = matrix[top_left.first][i];
        }

        //replace the top row
        for(int col = top_left.second, row = bottom_left.first; col < top_right.second; row--, col++)
        {
            matrix[top_left.first][col] = matrix[row][bottom_left.second];
        }

        //replace the left row
        for(int col = bottom_right.second, row = bottom_left.first; col > bottom_left.second; row--, col--)
        {
            matrix[row][bottom_left.second] = matrix[bottom_right.first][col];
        }

        //replace the bottom row
        for(int col = bottom_right.second, row = top_right.first; row < bottom_right.first; row++, col--)
        {
            matrix[bottom_left.first][col] = matrix[row][top_right.second];
        }

        //put the array back into the right side of the frame
        for(int col = top_right.second, row = top_right.first; row < bottom_right.first; row++)
            matrix[row][col] = tempArray[row];

    }

#endif

};