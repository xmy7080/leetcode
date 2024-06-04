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
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        if(root == null) return result
        var currentLevel = mutableListOf<TreeNode>(root)
        
        while (currentLevel.isNotEmpty()) {
            val nextLevel = mutableListOf<TreeNode>()
            currentLevel.forEach { node ->
                node.left?.let {nextLevel += it}
                node.right?.let {nextLevel += it}
            }
            result.add(currentLevel.map{it.`val`})
            currentLevel = nextLevel
        }
        return result
    }
}
