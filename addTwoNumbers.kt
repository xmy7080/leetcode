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
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var h1 = l1
        var h2 = l2
        var carry = 0
        var result = ListNode(0)
        var resultH = result
        while (h1 != null && h2 != null){
            val tmp = h1.`val` + h2.`val` + carry
            val newVal = tmp % 10
            carry = tmp / 10
            val newNode = ListNode(newVal)
            resultH.next = newNode
            h1 = h1.next
            h2 = h2.next
            resultH = resultH.next
        }

        while (h1 != null) {
            val tmp = h1.`val` + carry
            val newVal = tmp % 10
            carry = tmp / 10
            val newNode = ListNode(newVal)
            resultH.next = newNode
            h1 = h1.next
            resultH = resultH.next
        }
        while (h2 != null) {
            val tmp = h2.`val` + carry
            val newVal = tmp % 10
            carry = tmp / 10
            val newNode = ListNode(newVal)
            resultH.next = newNode
            h2 = h2.next
            resultH = resultH.next
        }
        if (carry != 0) {
            val newNode = ListNode(carry)
            resultH.next = newNode
        }
        return result.next
    }
}
