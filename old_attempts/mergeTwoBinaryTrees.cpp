//Defined structure
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

//https://leetcode.com/problems/merge-two-binary-trees/

/*
            Input: 
                Tree 1                     Tree 2                  
                   1                         2                             
                  / \                       / \                            
                 3   2                     1   3                        
                /                           \   \                      
               5                             4   7                  
            Output: 
            Merged tree:
                  3
                 / \
                4   5
               / \   \ 
              5   4   7
*/

#define SOL 3

/*
    SOL 1 - 52 ms / 27.2 MB => ~64% better complexity than previous solutions/79% than previous memory usage
    SOL 2 - 44 ms / 21.8 MB
    SOL 3 - 36 ms / 21.8 MB => 97% better complexity than previous solutions/91% than previous memory usage
*/

class Solution
{
public:
#if SOL == 1
    TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2)
    {
        if (t1 == nullptr && t2 == nullptr)
            return nullptr;
        else if (t1 == nullptr && t2 != nullptr)
            return t2;
        else if (t1 != nullptr && t2 == nullptr)
            return t1;
        else
            return inorderTraversal(t1, t2);
    }

    // Recursive algorithm to add overlapping nodes together of two trees.
    TreeNode *inorderTraversal(TreeNode *t1, TreeNode *t2)
    {
        // 3 base cases to check for null values
        if (t1 == nullptr && t2 == nullptr)
            return nullptr;
        else if (t1 == nullptr && t2 != nullptr)
            return t2;
        else if (t1 != nullptr && t2 == nullptr)
            return t1;
        else
        {
            TreeNode *newNode = new TreeNode();

            // using inorder traversal to connect new nodes
            newNode->left = inorderTraversal(t1->left, t2->left);
            newNode->val = t1->val + t2->val;
            newNode->right = inorderTraversal(t1->right, t2->right);

            return newNode;
        }
    }
#endif

#if SOL == 2
    TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2)
    {
        if (t1 == nullptr && t2 == nullptr)
            return nullptr;
        else if (t1 == nullptr && t2 != nullptr)
            return t2;
        else if (t1 != nullptr && t2 == nullptr)
            return t1;
        else
            return inorderTraversal(t1, t2);
    }

    // Recursive algorithm to add overlapping nodes together of two trees.
    TreeNode *inorderTraversal(TreeNode *t1, TreeNode *t2)
    {
        // 3 base cases to check for null values
        if (t1 == nullptr && t2 == nullptr)
            return nullptr;
        else if (t1 == nullptr && t2 != nullptr)
            return t2;
        else if (t1 != nullptr && t2 == nullptr)
            return t1;
        else
        {
            // using inorder traversal to connect new nodes
            t2->left = inorderTraversal(t1->left, t2->left);
            t2->val = t1->val + t2->val;
            t2->right = inorderTraversal(t1->right, t2->right);

            return t2;
        }
    }
#endif

#if SOL == 3
    TreeNode *mergeTrees(TreeNode *t1, TreeNode *t2)
    {
        // 3 base cases to check for null values
        if (t1 == nullptr) return t2;
        if (t2 == nullptr) return t1;
        // using inorder traversal to connect new nodes
        t1->left = mergeTrees((t1) ? t1->left : nullptr, (t2) ? t2->left : nullptr);
        t1->val = t1->val + t2->val;
        t1->right = mergeTrees((t1) ? t1->right : nullptr, (t2) ? t2->right : nullptr);

        return t1;
    }
#endif
};