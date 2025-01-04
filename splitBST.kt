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
// idea is, if a node has bigger value than the target, the itself with right subtree must be in the bigger split tree, if a node is smaller, then itself with left subtree must be in the smaller split tree
// we need one origin node and one current node for the smaller and the bigger tree head respectively, when instantiate we set all of them null, 
// for small node scenario, we traverse down its right subtree because there could be node bigger than target, for bigger node scenario we traverse its left subtree because there could node smaller than the target
// for exact node value, we can stop with node + node.left to the smaller tree, and entire node.right to the bigger tree.
class Solution {
    fun splitBST(originRoot: TreeNode?, target: Int): Array<TreeNode?> {
        var biggerTree: TreeNode? = null
        var biggerNode: TreeNode? = null
        var smallerTree: TreeNode? = null
        var smallerNode: TreeNode? = null
        fun dfs(root: TreeNode?){
            if(root == null) return
            if(root.`val` < target){
                if(smallerTree == null){
                    smallerTree = root
                } else {
                    smallerNode!!.right = root
                }
                smallerNode = root
                val tmpNode = root.right
                root.right = null
                dfs(tmpNode)
            } else if (root.`val` > target){
                if(biggerTree == null){
                    biggerTree = root
                } else {
                    biggerNode!!.left = root
                }
                biggerNode = root
                val tmpNode = root.left
                root.left = null
                dfs(tmpNode)
            } else{ // ==
                // println("in equal case, root = " + root.`val`)
                if(smallerTree == null){
                    smallerTree = root
                } else {
                    smallerNode!!.right = root
                }
                if(biggerTree == null){
                    biggerTree = root.right
                } else {
                    biggerNode!!.left = root.right
                }
                root.right = null // subtree should not contain a right subtree anymore
                // println("in equal case, root right = " + root.right )
            }
        }
        dfs(originRoot)
        return arrayOf<TreeNode?>(smallerTree, biggerTree)
    }
}
