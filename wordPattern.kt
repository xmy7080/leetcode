class Solution {
    fun wordPattern(pattern: String, s: String): Boolean {
        val mapping = hashMapOf<Char, String>()
        val words = s.split(' ')
        if (pattern.length != words.size) return false
        words.forEachIndexed{i, word ->
            if(mapping.containsKey(pattern[i])){
                if(mapping[pattern[i]]!! != word) return false
            } else{
                mapping[pattern[i]] = word
            }
        }
        return mapping.values.toSet().size == mapping.keys.toSet().size
    }
}
