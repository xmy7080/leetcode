class Solution {
    fun findRepeatedDnaSequences(s: String): List<String> {
        val set = mutableSetOf<Int>()
        val result = mutableSetOf<String>()
        val BASE = 4
        val L = 10
        val APowerToL = Math.pow(BASE.toDouble(), L.toDouble()).toInt()
        val map = mapOf<Char, Int>('A' to 0, 'C' to 1, 'G' to 2, 'T' to 3)
        val numArray = IntArray(s.length)
        for(i in 0 until s.length){
            numArray[i] = map[s[i]]!!
        }

        var currHash = 0
        for(start in 0 until s.length - L + 1){
            if(start != 0){
                currHash = currHash * BASE - numArray[start-1] * APowerToL + numArray[start + L-1]
            } else{
                repeat(L){index -> currHash = currHash * BASE + numArray[index]}
            }
            if(currHash in set) result.add(s.substring(start, start + L))
            else set.add(currHash)
        }
        return result.toList()
    }
}
