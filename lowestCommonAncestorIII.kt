// optimized way doing this, solution refers to approach 3 in https://leetcode.com/problems/intersection-of-two-linked-lists/editorial/
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *		var left: TreeNode? = null
 *		var right: TreeNode? = null
 *		var parent: Node? = null
 * }
 */

class Solution {
    fun lowestCommonAncestor(p: Node?, q: Node?): Node? {
        var a = p
        var b = q
        while(a != b){
            a = a?.parent ?: q
            b = b?.parent ?: p
        }
        return a
    }
}
// naive hashset way of doing this
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *		var left: TreeNode? = null
 *		var right: TreeNode? = null
 *		var parent: Node? = null
 * }
 */
// try it with intersection of two sets
class Solution {
    fun lowestCommonAncestor(p: Node?, q: Node?): Node? {
        var pn = p
        var qn = q
        var pathP = mutableSetOf<Int>()
        var pathQ = mutableSetOf<Int>()
        while (pn != null || qn != null) {
            pn?.let { pathP.add(it.`val`)}
            qn?.let { pathQ.add(it.`val`)}
            val inter: Set<Int> = pathP.intersect(pathQ)
            if (inter.isNotEmpty()) return Node(inter.first())

            if (pn != null) pn = pn.parent
            if (qn != null) qn = qn.parent
        }
        return Node(0)
    }
}
