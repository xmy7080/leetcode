/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        if(head == null ) return head
        if(head?.next == null && n == 1) return null
        var curr = head
        var count = n +1
        while(curr != null && count > 0){
            curr = curr?.next
            count --
        }
        var prev = head
        if(curr == null && count == 1){ // when n == size of list, the head need to be removed
            val next = prev?.next
            prev?.next = null
            return next
        }
        else if(curr != null && count == 0){ // when n < size of list, prev need to move down
            while(curr != null){
                curr = curr?.next
                prev = prev?.next
            }
        }
        val toRemove = prev?.next
        prev?.next = toRemove?.next
        toRemove?.next = null
        return head
    }
}
