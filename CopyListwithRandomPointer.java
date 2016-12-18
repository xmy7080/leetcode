/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        //the ultimate solution, insert each copy node in next of original node, do the random pointer copy, and extract the dup list from the double-lengthed list
        	RandomListNode iter = head, next;

	// First round: make copy of each node,
	// and link them together side-by-side in a single list.
	while (iter != null) {
		next = iter.next;

		RandomListNode copy = new RandomListNode(iter.label);
		iter.next = copy;
		copy.next = next;

		iter = next;
	}

	// Second round: assign random pointers for the copy nodes.
	iter = head;
	while (iter != null) {
		if (iter.random != null) {
			iter.next.random = iter.random.next;
		}
		iter = iter.next.next;
	}

	// Third round: restore the original list, and extract the copy list.
	iter = head;
	RandomListNode pseudoHead = new RandomListNode(0);
	RandomListNode copy, copyIter = pseudoHead;

	while (iter != null) {
		next = iter.next.next;

		// extract the copy
		copy = iter.next;
		copyIter.next = copy;
		copyIter = copy;

		// restore the original list
		iter.next = next;

		iter = next;
	}

	return pseudoHead.next;
        //second answer with o(n) space and o(n) time, copy the whole list first, then the next and random pointers
        //   if (head == null) return null;
  
        //     Map<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
  
        //     // loop 1. copy all the nodes
        //     RandomListNode node = head;
        //     while (node != null) {
        //         map.put(node, new RandomListNode(node.label));
        //         node = node.next;
        //       }
  
        //     // loop 2. assign next and random pointers
        //     node = head;
        //     while (node != null) {
        //         map.get(node).next = map.get(node.next);
        //         map.get(node).random = map.get(node.random);
        //         node = node.next;
        //     }
  
        //   return map.get(head);
          
          
        //total clone map idea, but is slow
        // if(head == null) return head;
        // Queue<RandomListNode> q = new LinkedList<RandomListNode>();
        // q.offer(head);
        // HashMap<RandomListNode,RandomListNode> hm = new HashMap<RandomListNode,RandomListNode>();
        // RandomListNode newhead = new RandomListNode(head.label);
        // hm.put(head,newhead);
        // while(!q.isEmpty() ){
        //     RandomListNode n = q.poll();
        //     RandomListNode next = n.next;
        //     if(next != null){
        //         if(hm.containsKey(next) )
        //             hm.get(n).next = hm.get(next);
        //         else{
        //             RandomListNode newnext = new RandomListNode(next.label);
        //             hm.get(n).next = newnext;
        //             hm.put(next,newnext);
        //             q.offer(next);
        //         }
        //     }
        //     RandomListNode rand = n.random;
        //     if(rand != null){
        //         if(hm.containsKey(rand) )
        //             hm.get(n).random = hm.get(rand);
        //         else{
        //             RandomListNode newrand = new RandomListNode(rand.label);
        //             hm.get(n).random = newrand;
        //             hm.put(rand,newrand);
        //             q.offer(rand);
        //         }
        //     }
        // }
        // return newhead;
    }
}