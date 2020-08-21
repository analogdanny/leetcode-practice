//https://leetcode.com/problems/word-search/

/*
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
    are those horizontally or vertically neighboring. The same letter cell may not be used more than 
    once.

    Example:
        board =
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
        ]

        Given word = "ABCCED", return true.
        Given word = "SEE", return true.
        Given word = "ABCB", return false.
*/

#include <vector>
#include <stack>
#include <utility>
#include <iostream>

class Solution
{
public:
    bool exist(vector<vector<char>> &board, string word)
    {
        stack<pair<int, int>> st;
        int s_iter = 0, j = 0, i = 0, k = 0, l = 0;
        bool init_loc = false;
        pair<int, int> top, loc;

        // Find the first character in the board matching the word's first character
        // and save the location.

        while (s_iter < word.length())
        {
            // Where we are in the board array
            loc = {i, j};

            // If a correlating character is valid and found
            if (board[i][j] == word[s_iter] && top != loc)
            {
                board[i][j] = '*';
                s_iter++;
                st.push({i, j});
                top = st.top();
                cout << top.first;
                cout << ", ";
                cout << top.second;
                cout << endl;
            }

            if (s_iter == word.length())
                break;

            // Checking ^, v, <, > for next possible location of valid character.
            if (i + 1 < board.size() && board[i + 1][j] == word[s_iter] && top.first != i + 1 )
            {
                i++;
            }
            else if (i - 1 >= 0 && board[i - 1][j] == word[s_iter] && top.first != i - 1 )
            {
                i--;
            }
            else if (j + 1 < board[i].size() && board[i][j + 1] == word[s_iter] && top.second != j + 1 )
            {
                j++;
            }
            else if (j - 1 >= 0 && board[i][j - 1] == word[s_iter] && top.second != j - 1 )
            {
                j--;
            }
            else // find next starting position
            {
                //variable to find an initial location
                init_loc = false;

                //clear stack
                while (!st.empty())
                    st.pop();

                for (k; k < board.size(); k++)
                {
                    for (l; l < board[k].size(); l++)
                    {
                        if (board[k][l] == word[s_iter])
                        {
                            board[i][j] = '*';
                            s_iter++;
                            st.push({k, l});
                            top = st.top();
                            init_loc = true;
                            cout << top.first;
                            cout << ", ";
                            cout << top.second;
                            cout << endl;
                            break;
                        }
                    }
                    if (init_loc)
                        break;
                }

                if (!init_loc)
                    return false;
            }
        }

        return true;
    }
};