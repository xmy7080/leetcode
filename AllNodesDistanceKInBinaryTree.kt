/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun distanceK(root: TreeNode?, target: TreeNode?, k: Int): List<Int> {
        val res = mutableListOf<Int>()
        fun helper(node: TreeNode?, distance: Int?): Int?{
            if(node == null) return node
            if(distance != null){ //distance passed down from up above
                if(distance!! == k) res.add(node.`val`)
                if(distance!! < k){
                    helper(node.left, distance!! + 1)
                    helper(node.right, distance!! + 1)
                }
                return null
            } else{ // NO distance passed down from up above
                if(node?.`val` == target?.`val`){ // curr node is target node
                    if(k == 0) {
                        res.add(node.`val`)
                    } else {
                        helper(node.left, 1)
                        helper(node.right, 1)
                    }
                    return 1
                } else { // curr node isn't target node, keep search downward
                    val left = helper(node.left, null)
                    val right = helper(node.right, null)
                    if(left != null){
                        if(left!! == k) res.add(node.`val`)
                        if(left!! < k){
                            helper(node.right, left!! + 1)
                            return left!! + 1
                        } else return null
                    } else if(right != null){
                        if(right!! == k) res.add(node.`val`)
                        if(right!! < k){
                            helper(node.left, right!! + 1)
                            return right!! + 1
                        } else return null
                    } else{ // neither left nor right has found target number, or both has longer distance than k
                        return null
                    }
                }
            }
        }
        helper(root, null)
        return res
    }
}
