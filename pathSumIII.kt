// inspired by subarray sum equals to k, https://leetcode.com/problems/subarray-sum-equals-k/editorial/
// difference is we need to remove the curr prefix sum by the end of each recursion.
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
    fun pathSum(root: TreeNode?, targetSum: Int): Int {
        val map = mutableMapOf<Long, Int>(0L to 1)
        var result = 0
        fun dfs(node: TreeNode, prevSum: Long, map: MutableMap<Long, Int>): Unit {
            val sum = prevSum + node.`val`
            if (map.contains(sum - targetSum)){
                result += map.getOrDefault(sum - targetSum, 0)
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1)
            if(node.left != null) dfs(node.left!!, sum, map)
            if(node.right != null) dfs(node.right!!, sum, map)

            //remove the curr prefix sum by the end of each recursion. to prevent contamination
            map.put(sum, map.getOrDefault(sum, 0) - 1)
        }

        if(root != null) dfs(root!!, 0, map)
        return result
    }
}
