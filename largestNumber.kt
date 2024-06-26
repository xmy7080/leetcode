class Solution {
    fun largestNumber(nums: IntArray): String {
        val strBeforeZeroCheck = nums.toList().sortedWith(Comparator<Int> {a, b -> compareSemantic(a, b) }).reversed()
        if (strBeforeZeroCheck[0] == 0) return "0" // take care of the [0,0] scenario
        return strBeforeZeroCheck.joinToString("")
    }
    fun compareSemantic(a: Int, b: Int): Int {
        val astr = a.toString()
        val bstr = b.toString()
        return (astr + bstr).compareTo(bstr + astr)
        // commented is not the right comparator, it failed the case [34323,3432]
        // var i = 0
        // var j = 0
        // while ( true ) {
        //     if (astr[i] > bstr[j]) return 1
        //     else if (astr[i] < bstr[j]) return -1
        //     else {
        //         if (i == astr.length -1 && j == bstr.length -1) break
        //         if (i+1 < astr.length) i ++
        //         if (j+1 < bstr.length) j ++
        //     }
        // }
        // return 1
    }
}
