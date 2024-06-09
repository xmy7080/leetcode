// to find Kth largest => hold k-1 elements in the base of of the min heap, then the top is the Kth largest
//                     => OR, put all elements in a max heap and pop k-1 times, then the peak is the Kth Largest
// to find Kth smallest => holde k-1 elements in the base of the max heap, then the top is the Kth smallest
//                      => OR, put all elments in a min heap, then pop k-1 times, then the peak would be Kth smallest
class Solution {
    // solution with min heap
    // fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
    //     val compareByDistance: Comparator<IntArray> = compareBy {distance(it)}
    //     var pq = PriorityQueue<IntArray>(compareByDistance)
    //     points.forEach{ point ->
    //         pq.add(point)
    //     }
    //     var result = mutableListOf<IntArray>()
    //     for (i in 0 until k) {
    //         result += pq.poll()
    //     }
    //     return result.toTypedArray()
    // }

// solution with max heap
    fun kClosest(points: Array<IntArray>, k: Int): Array<IntArray> {
        val compareByDistance: Comparator<IntArray> = compareBy { -1 * distance(it)}
        var pq = PriorityQueue<IntArray>(compareByDistance)
        points.forEach{ point ->
            pq.add(point)
            if (pq.size > k) pq.poll()
        }
        return pq.toTypedArray()
    }

    fun distance(point: IntArray): Int {
        return point[0] * point[0] + point[1] * point[1]
    }
}
