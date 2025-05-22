// used this brilliant recursive solution, and partition is using binary approach
// https://leetcode.com/problems/merge-k-sorted-lists/solutions/10522/my-simple-java-solution-use-recursion/?envType=company&envId=verkada&favoriteSlug=verkada-more-than-six-months
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        return partition(lists, 0, lists.length -1);
    }

    public ListNode partition(ListNode[] lists, int s, int e) {
        if(s == e) return lists[s];
        if(s < e){
            int p = s+ (e-s)/2;
            ListNode part1 = partition(lists, s, p);
            ListNode part2 = partition(lists, p+1, e);
            return merge(part1, part2);
        }
        return null;
    }

    public ListNode merge(ListNode a, ListNode b){
        if(a == null) return b;
        if(b == null) return a;
        if(a.val < b.val){
            a.next = merge(a.next, b);
            return a;
        } else{
            b.next = merge(a, b.next);
            return b;
        }
    }
}
