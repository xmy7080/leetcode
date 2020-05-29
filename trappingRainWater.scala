import scala.annotation.tailrec

object Solution {
    def trap(height: Array[Int]): Int = {
        @tailrec
        def loop(l: Int, r: Int, lH: Int, rH: Int, total: Int): Int = {
            if (l == r) total
            else if (lH < rH) loop(l+1, r, math.max(lH, height(l+1)), rH, total + lH - height(l) )
            else              loop(l, r-1, lH, math.max(rH, height(r-1)), total + rH - height(r) )
        }
        if (height.isEmpty) 0 else loop(0, height.length -1, height(0), height(height.length -1), 0 )
    }
}
