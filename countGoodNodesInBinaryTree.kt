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
    fun goodNodes(root: TreeNode?): Int {
        var count = 0
        fun dfs(node: TreeNode, pathMax: Int): Unit {
            var max = node.`val`
            if (pathMax > node.`val`) {
                max = pathMax 
            } else count ++

            if (node.left != null) dfs(node.left, max)
            if (node.right != null) dfs(node.right, max)
        }
        
        root?.let{ dfs(it, it.`val`) }
        return count
    }
}
