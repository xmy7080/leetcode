class Solution {
    fun toGoatLatin(sentence: String): String {
        val words = sentence.split(" ")
        val sbs = mutableListOf<String>()
        words.forEachIndexed{idx, word ->
            val newSB = convert(word)
            repeat(idx+1) {newSB.append('a')}
            sbs.add(newSB.toString())
        }
        return sbs.joinToString(" ")
    }
    private fun convert(word: String): StringBuilder{
        val vowels = setOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        val sb = StringBuilder(word)
        if(word[0] !in vowels){
            sb.deleteCharAt(0)
            sb.append(word[0])
        }
        sb.append("ma")
        return sb
    }
}
