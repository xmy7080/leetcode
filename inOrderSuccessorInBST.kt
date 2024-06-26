/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun inorderSuccessor(root: TreeNode?, p: TreeNode?): TreeNode? {
        val stk = ArrayDeque<TreeNode>()
        var node = root
        var flip = false
        while (stk.isNotEmpty() || node != null) {
            while (node != null){
                stk.addFirst(node!!)
                node = node!!.left
            }
            node = stk.removeFirst()
            if (flip) return node
            if (p!!.`val` == node!!.`val`) flip = true
            node = node.right
        }
        return null
    }
}
