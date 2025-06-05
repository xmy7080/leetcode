/**
 * Example:
 * var ti = Node(5)
 * var v = ti.`val`
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var next: Node? = null
 *     var random: Node? = null
 * }
 */

class Solution {
    fun copyRandomList(node: Node?): Node? {
        val map = HashMap<Node, Node>()
        var curr = node

        // copy all the nodes first
        while(curr != null){
            map[curr] = Node(curr.`val`)
            curr = curr.next
        }
        curr = node
        //copy all the next and random pointer
        while(curr != null){
            map.get(curr)!!.next = map.get(curr.next)
            map.get(curr)!!.random = map.get(curr.random)
            curr = curr.next
        }
        return map.get(node)
    }
}
