class Solution {
    fun reverseString(s: String): String {
        println(s)
        var countForwardUS = 0
        for ( c in s){
            if (c != '_') break
            countForwardUS ++
        }
        var countBackwardUS = 0
        for ( i in s.length -1 downTo 0){
            if (s[i] != '_') break
            countBackwardUS ++
        }
        var words: MutableList<String> = s.split("_+".toRegex()).filterNot{it.isBlank()}.toMutableList()
        println("size of words is  " + words.size)
        for (i in 1 until words.size){
            words[i] = words[i].capitalize()
            println(words[i])
        }
        println("_".repeat(countForwardUS) + words.joinToString("") + "_".repeat(countBackwardUS))
    }
}
