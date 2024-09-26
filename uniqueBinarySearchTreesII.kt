// brutal dfs solution, make copy did the tree copy work intuitively
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
    fun makeCopy(node: TreeNode?): TreeNode?{
        if(node == null) return null
        val root = TreeNode(node.`val`)
        root.left = makeCopy(node.left)
        root.right = makeCopy(node.right)
        return root
    }
    fun generateTrees(n: Int): List<TreeNode?> {
        val startArr = IntArray(n){it + 1}
        fun dfs(numbers: IntArray): List<TreeNode?> {
            val res = mutableListOf<TreeNode?>()
            if(numbers.size == 0){
                return listOf<TreeNode?>(null)
            }
            if(numbers.size == 1){
                return listOf<TreeNode?>(TreeNode(numbers[0]))
            }
            for (i in 0 until numbers.size){
                val leftSubtrees = dfs(numbers.slice(0 .. i-1).toIntArray())
                val rightSubtrees = dfs(numbers.slice(i+1 .. numbers.size-1 ).toIntArray())
                for (leftSub in leftSubtrees){
                    for (rightSub in rightSubtrees){
                        val root = TreeNode(numbers[i])
                        root.left = makeCopy(leftSub)
                        root.right = makeCopy(rightSub)
                        res.add(root)
                    }
                }
            }
            return res
        }
        
        return dfs(startArr)
    }
}
