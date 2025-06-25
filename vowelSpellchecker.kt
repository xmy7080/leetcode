class Solution {
    fun spellchecker(wordlist: Array<String>, queries: Array<String>): Array<String> {
        val exact = mutableSetOf<String>()
        val lowercaseMap = mutableMapOf<String, String>()
        val vowelMap = mutableMapOf<String, String>()

        for(word in wordlist){
            exact.add(word)
            lowercaseMap.putIfAbsent(word.lowercase(), word)
            vowelMap.putIfAbsent(maskVowel(word), word)
        }
        val res = mutableListOf<String>()
        for(query in queries){
            if(query in exact) res.add(query)
            else if(query.lowercase() in lowercaseMap) res.add(lowercaseMap.getOrDefault(query.lowercase(), ""))
            else if(maskVowel(query) in vowelMap) res.add(vowelMap.getOrDefault(maskVowel(query), ""))
            else res.add("")
        }
        return res.toTypedArray()
    }
    fun maskVowel(word: String): String{
        val sb = StringBuilder("")
        val vowels = setOf<Char>('a', 'e', 'i', 'o', 'u')
        for(c in word.lowercase()){
            if(c in vowels) sb.append('*')
            else sb.append(c)
        }
        return sb.toString()
    }
}
