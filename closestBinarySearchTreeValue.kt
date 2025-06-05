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
    fun closestValue(root: TreeNode?, target: Double): Int {
        var res = root!!.`val`

        fun helper(root: TreeNode?) {
            if(root == null) return
            val value = root!!.`val`
            if(Math.abs(res - target) > Math.abs(value - target)) res = value
            else if (Math.abs(res - target) == Math.abs(value - target)) res = minOf(value, res) // this line taken care of the case of tie breaker, we always take the value lesser if two are with same distance
            if(value.toDouble() == target) {
                res = value
                return
            }
            else if(target > value) helper(root.right)
            else helper(root.left)
        }

        helper(root)
        return res
    }
}
