class Solution {
    fun successfulPairs(spells: IntArray, potions: IntArray, success: Long): IntArray {
        val sortp = potions.sorted()
        var result = IntArray(spells.size){0}
        spells.forEachIndexed{idx, spell ->
            var l = 0
            var r = sortp.size
            while (l < r){ // when loop stops, l == r
                var mid = l + (r-l)/2
                if (spell.toLong() * sortp[mid] >= success){// goal is to find the first index, which product is >= success
                    r = mid // cannot be r = mid -1, could end up on a index which product is < success
                } else {
                    l = mid + 1
                }
            }
            result[idx] = sortp.size - l
        }
        // self solution took too much +1 -1 tries. Passed but consume too much time
        // spells.forEachIndexed{idx, spell ->
        //     var left = 0
        //     var right = sortp.size -1
        //     while (left <= right){
        //         var mid = (left + right)/2
        //         if (spell.toLong() * sortp[mid] < success) {
        //             if (mid+1 < sortp.size && spell.toLong() * sortp[mid+1] >= success) {
        //                 result[idx] = sortp.size -1 - mid //count mid +1 until size -1
        //                 break
        //             }
        //             left = mid + 1
        //         } else {// >= success
        //             if (mid == 0) {
        //                 result[idx] = sortp.size
        //                 break
        //             }
        //             if (mid -1 >=0 && spell.toLong() * sortp[mid-1] < success) {
        //                 result[idx] = sortp.size - mid // count mid until size -1
        //                 break
        //             }
        //             right = mid -1
        //         }
        //     }
        // }
        return result
    }
}
