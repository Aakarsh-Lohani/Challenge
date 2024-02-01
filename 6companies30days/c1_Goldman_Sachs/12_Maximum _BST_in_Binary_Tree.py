#https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
"""
1373. Maximum Sum BST in Binary Tree
Hard

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 

Constraints:

The number of nodes in the tree is in the range [1, 4 * 10^4].
-4 * 10^4 <= Node.val <= 4 * 10^4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Here's the solution to get the maxSumBST using post order

class Solution:
  def maxSumBST(self, root):
    self.res = 0
    def dfs(node):
      if not node: return 0, float('inf'), float('-inf'), True
      l, r = dfs(node.left), dfs(node.right)
      if l[3] and r[3] and node.val > l[2] and node.val < r[1]:
        self.res = max(self.res, node.val + l[0] + r[0])
        return node.val + l[0] + r[0], min(l[1], node.val), max(r[2], node.val), True
      else: return 0, 0, 0, False
    dfs(root)
    return self.res