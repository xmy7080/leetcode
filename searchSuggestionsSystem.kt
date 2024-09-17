//induction from trie tree (prefix tree) solution
//also used a dfs search for the most 3 small lexicography results
class TrieNode {
    val children = Array<TrieNode?>(26) {null}
    var word: String? = null
}
class Solution {
    val root = TrieNode()
    
    fun add(word: String) {
        var node = root
        for(c in word){
            val index = c - 'a' // convert char to index in lexicography order, 'a' -> 0 and 'b' -> 1, etc
            if (node.children[index] == null) node.children[index] = TrieNode()
            node = node.children[index]!!
        }
        node.word = word
    }

    fun find3Min(node: TrieNode): List<String>{
        var max = 3
        val res = mutableListOf<String>()
        fun dfs(node: TrieNode){
            if(node.word != null){
                res.add(node.word!!)
                max -= 1
                if ( max == 0) return
            }
            for (i in node.children.indices){
                if(node.children[i] != null){
                    dfs(node.children[i]!!)
                }
                if ( max == 0) return
            }
        }
        dfs(node)
        return res
    }

    fun suggestedProducts(products: Array<String>, searchWord: String): List<List<String>> {
        for (product in products){
            add(product)
        }
        var res = mutableListOf<List<String>>()
        var node = root
        for (c in searchWord){
            
            val index = c - 'a'
            if(node.children[index] == null){
                res.add(emptyList())
                break
            }
            node = node.children[index]!!
            val tmp = find3Min(node)
            res.add(tmp)
        }
        for(i in res.size+1 .. searchWord.length){
            res.add(emptyList())
        }
        return res
    }
}
