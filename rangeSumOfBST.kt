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
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        if(root == null || low > high) return 0
        val notNullNode = root!!
        return if(notNullNode.`val` in low .. high) {
            notNullNode.`val` + 
                rangeSumBST(notNullNode.left, low, notNullNode.`val`-1) + 
                rangeSumBST(notNullNode.right, notNullNode.`val`+1, high)
        } else if(notNullNode.`val` < low){
            rangeSumBST(notNullNode.right, low, high)
        } else rangeSumBST(notNullNode.left, low, high)
    }
}

// original solution with no pruning
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
    var l: Int = 0
    var h: Int = 0
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        l = low
        h = high
        return helper(root)
    }
    fun helper(node: TreeNode?): Int {
        if (node == null) return 0
        if (node!!.`val` >= l && node!!.`val` <= h) return node!!.`val` + helper(node!!.left) + helper(node!!.right)
        else if(node!!.`val` < l) return helper(node!!.right)
        else return helper(node!!.left)
    }
}
