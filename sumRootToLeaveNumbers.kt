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
class Solution {
    var result = 0
    fun sumNumbers(root: TreeNode?): Int {
        helper(root!!, 0)
        return result
    }

    fun helper(node: TreeNode, topVal: Int) {
        val tempTopVal = topVal + node.`val`
        if (node.left == null && node.right == null) { // find leave node
            result += tempTopVal
            return
        }
        if (node.left != null) helper(node.left, tempTopVal * 10)
        if (node.right != null) helper(node.right, tempTopVal * 10)
        return
    }
}
