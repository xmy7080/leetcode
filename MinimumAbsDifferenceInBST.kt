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
    fun getMinimumDifference(root: TreeNode?): Int {
        var res = Int.MAX_VALUE
        var lastVal: Int? = null
        fun dfs(node: TreeNode): Unit {
            if(node.left != null) dfs(node.left)
            val diff = lastVal?.let{node.`val` - it}
            if(diff != null && diff < res) res = diff
            lastVal = node.`val`
            if(node.right != null) dfs(node.right)
        }
        dfs(root!!)
        return res
    }
}
