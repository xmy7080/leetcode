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
    fun findLeaves(root: TreeNode?): List<List<Int>> {
        // val result = mutableListOf<List<Int>>()
        val map = mutableMapOf<Int, MutableList<Int>>()

        fun dfs(node: TreeNode?): Int{
            if(node == null) return -1 //null is not a leave
            val distanceLeft = dfs(node?.left)
            val distanceRight = dfs(node?.right)
            val furtherestDistanceToLeaves = max(distanceLeft, distanceRight) + 1 //leave node will have distance = 0
            // if(result.size > furtherestDistanceToLeaves){
            //     val muteList = result.get(furtherestDistanceToLeaves).toMutableList()
            //     muteList.add(node.`val`)
            //     result[furtherestDistanceToLeaves] = muteList.toList()
            // } else{
            //     val muteList = listOf(node.`val`)
            //     result.add(muteList)
            // }
            map.getOrPut(furtherestDistanceToLeaves){mutableListOf()}.add(node.`val`)
            return furtherestDistanceToLeaves
        }
        dfs(root)
        // return result.toList()
        return map.values.toList()
    }
}
