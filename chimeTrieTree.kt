class TrieNode() {
    val children = HashMap<Char, TrieNode>()
    var isWord = false
}
class Trie() {
    val root = TrieNode()
    fun insert(word: String) {
        var node = root
        for (c in word){
            if (node.children.contains(c)){
                node = node.children[c]!!
            } else{
                val newNode = TrieNode()
                node.children.put(c, newNode)
                node = node.children[c]!!
            }
        }
        node.isWord = true
    }
// actual chime interview question, word break II with trie combined solution
    fun search(dummy: String): Boolean{
        // val number = "4663" // ["good"],["home"],["hood"]
        // val number = "2277" //["cars"],["bars"],["caps"]
        val number = "76638463" //["some"],["time"],["rome"],["sometime"],["so"],["me"]
        val res = mutableListOf<List<String>>()
        val tmp = mutableListOf<String>()
        fun dfs(index: Int){
            if(index == number.length){
                res.add(tmp.toList())
            } else{
                for(i in index + 1 .. number.length){
                    val subStr = number.substring(index, i)
                    for(matchWord in fetchPossibleWords(subStr)){
                        tmp.add(matchWord)
                        dfs(i)
                        tmp.removeAt(tmp.size - 1)
                    }
                }
            }
            return
        }
        dfs(0)
        res.forEach{
            println(" " + it.joinToString(","))
        }

        return false
    }
    
    val keyMap: Map<Char,String> = mapOf('2' to "abc", '3' to "def", '4' to "ghi", '5' to "jkl", '6' to "mno", '7' to "pqrs", '8' to "tuv", '9' to "wxyz" )
    //fetchPossibleWords should return list of strings
    fun fetchPossibleWords(number: String): List<String>{
        val res = mutableListOf<String>()
        fun dfs(tmp: StringBuilder, root: TrieNode, index: Int) {
            var node = root
            if(index == number.length){
                if(node.isWord){
                    res.add(tmp.toString())
                }
                return
            }
            val possibleChars = keyMap[number[index]] ?: ""
            for(c in possibleChars){
                if(node.children.contains(c)){
                    tmp.append(c)
                    dfs(tmp, node.children[c]!!, index + 1)
                    tmp.deleteCharAt(tmp.length -1)
                }
            }
            return
        }
        dfs(StringBuilder(""), root, 0)
        return res
    }


// original leetcode search function solution
    // fun search(word: String): Boolean {
    //     var node = root
    //     for (c in word){
    //         if (node.children.contains(c)) {
    //             node = node.children[c]!!
    //         } else{
    //             return false
    //         }
    //     }
    //     return node.isWord
    // }

    fun startsWith(prefix: String): Boolean {
        var node = root
        for (c in prefix){
            if (node.children.contains(c)) {
                node = node.children[c]!!
            } else{
                return false
            }
        }
        return true
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
