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
    var result = mutableListOf<List<Int>>()
    var colMap = mutableMapOf<Int, MutableList<Pair<Int,Int>>>()
    fun verticalOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return result
        helper(0, 0, root)
        var keys = colMap.keys
        val start = keys.min()
        val end = keys.max()
        for (idx in start .. end) {
            val tmpPairs: MutableList<Pair<Int,Int>> = colMap[idx]?: mutableListOf<Pair<Int,Int>>()
            val tmpList: List<Int> = tmpPairs.sortedBy{it.first}.map{it.second}
            result += tmpList
        }
        return result
    }

    fun helper(row: Int, colNumber: Int, node: TreeNode?) {
        if (node == null) return
        var currList = colMap[colNumber]?: mutableListOf<Pair<Int,Int>>()
        currList += Pair(row, node!!.`val`)
        colMap.put(colNumber, currList)
        if (node!!.left != null) helper(row + 1, colNumber - 1, node!!.left)
        if (node!!.right != null) helper(row + 1, colNumber + 1, node!!.right)
    }
}
