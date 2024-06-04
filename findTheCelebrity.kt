/* The knows API is defined in the parent class Relation.
      fun knows(a: Int, b: Int) : Boolean {} */

class Solution: Relation() {
    override fun findCelebrity(n: Int) : Int {
        var candidate = 0
        for (idx in 1 until n) {
            if (knows(candidate, idx)) candidate = idx
        }
        for (idx in 0 until n) {
            if (candidate == idx) {
                continue
            }
            if (knows(candidate, idx)) return -1
            if (!knows(idx, candidate)) return -1
        }
        return candidate
	}
}
