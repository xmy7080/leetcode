// similar to group acronym, this convert every str to a str starts with 'a' and maintaining its relative distance for the rest of str
// hence, "abc", "yza" and "xyz" will all ends up as "abc"
class Solution {
    fun groupStrings(strings: Array<String>): List<List<String>> {
        val res = mutableListOf<MutableList<String>>()
        val map = hashMapOf<String, MutableList<String>>()
        for(str in strings){
            val key = convert(str)
            val tmpList = map.getOrPut(key) {mutableListOf<String>()}
            tmpList.add(str)
        }
        for(entry in map){
            res.add(entry.value)
        }

        return res
    }
    private fun convert(str: String): String {
        val sb = StringBuilder("")
        sb.append('a')
        val shift: Int = str[0].code - 'a'.code

        for(i in 1 until str.length){
            val char = (((str[i].code - shift) % 26) + 'a'.code).toChar()
            // println("str i is ${str[i]}, shift is $shift, its converted to $char ")
            sb.append(char)
        }
        return sb.toString()
    }
}
