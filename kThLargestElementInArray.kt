// to find Kth largest => hold k-1 elements in the base of of the min heap, then the top is the Kth largest
//                     => OR, put all elements in a max heap and pop k-1 times, then the peak is the Kth Largest
// to find Kth smallest => holde k-1 elements in the base of the max heap, then the top is the Kth smallest
//                      => OR, put all elments in a min heap, then pop k-1 times, then the peak would be Kth smallest
//  kotlin code
class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        var pq = PriorityQueue<Int>()
        nums.forEach {
            pq.add(it)
            if (pq.size > k) pq.poll()
        }
        return pq.peek()
    }
}
