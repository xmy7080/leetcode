// solution follow from
// https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/3317557/kotlin-trie-with-recursive-search/
class TrieNode {
    var isWord: Boolean = false
    val children = Array<TrieNode?>(26){null}
}
class WordDictionary() {
    private val root = TrieNode()

    fun addWord(word: String) {
        var node = root
        for (i in word.indices) {
            val c = word[i] - 'a'
            if (node.children[c] == null){
                node.children[c] = TrieNode()
            }
            node.children[c]?.let{node = it}
        }
        node.isWord = true
    }

    fun search(word: String): Boolean = dfs(word, root, 0)

    private fun dfs(word: String, node: TrieNode, index: Int): Boolean {
        if (index == word.length) return node.isWord
        val c = word[index]
        return if (c == '.'){
            node.children.any {it != null && dfs(word, it, index + 1) }
        } else {
            node.children[c - 'a']?.let { dfs(word, it, index + 1) } ?: false
        }
    }

}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
