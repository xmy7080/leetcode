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
    fun partition(head: ListNode?, x: Int): ListNode? {
        val sStart = ListNode(0)
        var sLast = sStart
        val bStart = ListNode(0)
        var bLast = bStart
        var point = head
        while (point != null) {
            if (point!!.`val` < x){
                sLast.next = point
                sLast = point
                point = point.next
                sLast.next = null
            } else {
                bLast.next = point
                bLast = point
                point = point.next
                bLast.next = null
            }
        }
        sLast.next = bStart.next
        return sStart.next
    }
}
