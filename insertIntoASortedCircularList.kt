//editorial solution
/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var next: Node? = null
 * }
 */

class Solution {
    fun insert(head: Node?, insertVal: Int): Node? {
        if(head == null){
            val node = Node(insertVal)
            node.next = node
            return node
        }

        var prev = head
        var curr = head?.next
        var toInsert = false
        do{
            // case one, insert value in middle of prev and curr
            if(insertVal in prev!!.`val` .. curr!!.`val`){
                toInsert = true
            } else if(prev!!.`val` > curr!!.`val` && (insertVal > prev!!.`val` || insertVal < curr!!.`val`) ){
                toInsert = true
            }

            if(toInsert){
                val newNode = Node(insertVal)
                prev?.next = newNode
                newNode.next = curr
                return head
            }
            prev = curr
            curr = curr?.next
        }while(prev != head)

        val newNode = Node(insertVal)
        prev?.next = newNode
        newNode.next = curr
        return head
    }
}
