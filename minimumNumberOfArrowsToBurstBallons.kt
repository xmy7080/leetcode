// sort the intervals by left and then by right bound, from first interval find its overlapping neighbors, until the jth interval
// that do not overlap with it, account the arrow, update i = j and keep the loop
class Solution {
    fun isOverlap(right:Int, j: Int, ballons: List<IntArray>): Boolean{
        // ballons is sorted, so the overlap can be determined just by ahead interval right bound and behind interval left bound
        return !(right < ballons[j][0] )
    }
    fun findMinArrowShots(points: Array<IntArray>): Int {
        val ballons = points.sortedWith(compareBy<IntArray> ({it[0]}, {it[1]}))
        // ballons.forEach{b ->
        //     println("left " + b[0] + " right " + b[1])
        // }
        var i = 0
        var res = 0
        while (i < ballons.size){
            var left = ballons[i][0]
            var right = ballons[i][1]
            var j = i + 1
            while (j < ballons.size && isOverlap(right, j, ballons)){
                right = listOf(right, ballons[j][1]).min() // update combined "AND" intervals right bound
                j ++ // look at next intervals
            }
            i = j
            res ++
        }
        return res
    }
}

//https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/editorial/?envType=study-plan-v2&envId=leetcode-75
//editorial solution, sort the ballons by its RIGHT bound, then the next ballons is either
// starts before first ballon's end, it can burst together
// starts after first ballon's end, it cannot burst together, bump the arrow count and look at this new ballon
class Solution {
    fun findMinArrowShots(points: Array<IntArray>): Int {
        val ballons = points.sortedWith(compareBy<IntArray> ({it[1]}))
        // ballons.forEach{b ->
        //     println("left " + b[0] + " right " + b[1])
        // }
        var i = 0
        var res = 0
        while (i < ballons.size){
            var j = i + 1
            while (j < ballons.size && ballons[j][0] <= ballons[i][1]){
                j ++ // look at the next ballon
            }
            i = j
            res ++
        }
        return res
    }
}
