/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
// pay attention to the root node at each, level, its old left and right pointer should reset to null, otherwise there will be cycle in the new tree
class Solution {
    fun upsideDownBinaryTree(root: TreeNode?): TreeNode? {
        if(root?.left == null) return root
        else{
            val leftMost = upsideDownBinaryTree(root?.left)
            root?.left!!.left = root?.right
            root?.left!!.right = root!!
            root?.right = null
            root?.left = null
            return leftMost
        }
    }
}
