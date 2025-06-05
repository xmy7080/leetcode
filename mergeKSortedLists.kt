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
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        return partition(lists, 0, lists.size-1)
    }
    private fun partition(lists: Array<ListNode?>, s: Int, e: Int): ListNode?{
        if(s == e) return lists[s]
        else if (s < e){
            val m = s + (e-s)/2
            val part1 = partition(lists, s, m)
            val part2 = partition(lists, m+1, e)
            return merge(part1, part2)
        } 
        else return null
    }
    private fun merge(a: ListNode?, b: ListNode?): ListNode?{
        if(a == null) return b
        if(b == null) return a
        if(a!!.`val` < b!!.`val`) {
            a!!.next = merge(a?.next, b)
            return a
        } else {
            b!!.next = merge(a, b?.next)
            return b
        }
    }
}
