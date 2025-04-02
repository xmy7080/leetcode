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
