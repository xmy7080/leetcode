/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var left: Node? = null
 *     var right: Node? = null
 * }
 */

class Solution {
    // store the leftmost node as the head of linked list, also the last seen as the previous node
    var first: Node? = null
    var last: Node? = null
    fun helper(node: Node?) {
        if(node != null){
            helper(node!!.left)

            if(last != null){
                // link the previous node (last)
                // with the current one (node)
                last?.right = node
                node?.left = last
            } else {
                // keep the smallest node
                // to close double linked list later on
                first = node
            }
            last = node

            helper(node!!.right)
        }
    }
    fun treeToDoublyList(root:Node?): Node? {
        helper(root)

        first?.left = last
        last?.right = first
        return first
    }
}
