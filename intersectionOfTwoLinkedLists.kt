// refer to editorial solution III, also pay attention there could be case two list never intersect. 
// the solution brilliantly added a null phase during looping, so that when pointers finished 2 lists traversal, they will all concludes at a null
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
    fun getIntersectionNode(headA:ListNode?, headB:ListNode?):ListNode? {
        var a = headA
        var b = headB
        while(a != b){
            a = if(a== null) headB else a.next
            b = if(b== null) headA else b.next
        }
        return a
    }
}
