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
    var result = -100000000
    var found = false
    fun maxPathSum(root: TreeNode?): Int {
        helper(root)
        return if (result != -100000000) result else 0
    }

    fun helper(node: TreeNode?): Int {
        if (node == null) return 0
        else if (node.left == null && node.right == null) {
            result = max(node.`val`, result)
            return max(node.`val`, 0)
        }
        else if (node.left == null) {
            val rightVal = helper(node.right)
            val nodeVal = node.`val`
            val candidate = max(nodeVal + rightVal, nodeVal)
            result = max(result, candidate)
            return max(candidate, 0)
        }
        else if (node.right == null) {
            val leftVal = helper(node.left)
            val nodeVal = node.`val`
            val candidate = max(nodeVal + leftVal, nodeVal)
            result = max(result, candidate)
            return max(candidate, 0)
        }
        else {
            val leftMax = helper(node.left)
            val rightMax = helper(node.right)
            val candidateMaxPath = maxOf(
                maxOf(leftMax + rightMax + node.`val`, rightMax + node.`val`, leftMax + node.`val`),
                node.`val`)
            result = max(candidateMaxPath, result)
            return maxOf(
                maxOf(rightMax + node.`val`, leftMax + node.`val`),
                node.`val`, 0)
        }
    }
}
