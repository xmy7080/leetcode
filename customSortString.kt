class Solution {
    fun customSortString(order: String, s: String): String {
        val charCount = IntArray(26){0}
        for(c in s){
            charCount[c.toInt() - 'a'.toInt()] ++
        }
        val sb = StringBuilder("")
        for(c in order){
            val cIndex = c.toInt() - 'a'.toInt()
            val count = charCount[cIndex]
            repeat(count) {sb.append(c)}
            charCount[cIndex] = 0
        }
        charCount.forEachIndexed{idx, count->
            val count = charCount[idx]
            val char = ('a'.toInt()+idx).toChar()
            repeat(count) {sb.append(char)}
        }
        return sb.toString()
    }
}
