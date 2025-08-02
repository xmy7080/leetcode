// editorial solutiion #1
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
    fun isCompleteTree(root: TreeNode?): Boolean {
        root ?: return true
        var seenNull = false
        val queue = LinkedList<TreeNode?>()
        queue.addLast(root)
        while(queue.isNotEmpty()){
            val currNode = queue.removeFirst()
            if(seenNull && currNode != null) return false
            if(currNode == null) {
                seenNull = true
                continue
            }
            queue.addLast(currNode.left)
            queue.addLast(currNode.right)
        }
        return true
    }
}
