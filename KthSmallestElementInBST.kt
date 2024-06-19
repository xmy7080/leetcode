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
    // more clean approach and less space used
    fun kthSmallest(root: TreeNode?, k: Int): Int {
        val stk = ArrayDeque<TreeNode>()
        var node = root
        var count = 0
        while (true) {
            while (node != null) {
                stk.addFirst(node!!)
                node = node!!.left
            }
            node = stk.removeFirst()
            count ++
            if (count == k) return node.`val`
            node = node.right
            
        }
        return 0
    }

    // used stack for iteration and hashset for mark visited node
    // fun kthSmallest(root: TreeNode?, k: Int): Int {
    //     val stk = ArrayDeque<TreeNode>()
    //     val hset = HashSet<TreeNode>()
    //     stk.addFirst(root!!)
    //     var count = 0
    //     while (stk.isNotEmpty()) {
    //         val top = stk.first()
    //         if (top.left != null && top.left !in hset) {
    //             stk.addFirst(top.left!!)
    //         } else {
    //             stk.removeFirst()
    //             hset.add(top)
    //             count ++
    //             if (count == k) return top.`val`
    //             if (top.right != null && top.right !in hset) stk.addFirst(top.right!!)
    //         }
    //     }
    //     return 0
    // }
}
