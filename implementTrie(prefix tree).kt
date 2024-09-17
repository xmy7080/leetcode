//my personal solution
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

    fun search(word: String): Boolean {
        var node = root
        for (c in word){
            if (node.children.contains(c)) {
                node = node.children[c]!!
            } else{
                return false
            }
        }
        return node.isWord
    }

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
//another solution that uses 26 size array
/** Initialize your data structure here. */
class TrieNode {
    val children = Array<TrieNode?>(26) { null }
    var isWord = false
}

val trieTree = TrieNode()

/** Inserts a word into the trie. */
fun insert(word: String) {
    var p = trieTree

    for (w in word) {
        val i = w - 'a'
        if (p.children[i] == null) p.children[i] = TrieNode()
        p = p.children[i]!!
    }
    p.isWord = true
}

/** Returns if the word is in the trie. */
fun search(word: String): Boolean {
    var p = trieTree
    
    for (w in word) {
        val i = w - 'a'
        if (p.children[i] == null) return false
        p = p.children[i]!!
    }
    return p.isWord
}

/** Returns if there is any word in the trie that starts with the given prefix. */
fun startsWith(prefix: String): Boolean {
    var p = trieTree
    
    for (w in prefix) {
        val i = w - 'a'
        if (p.children[i] == null) return false
        p = p.children[i]!!
    }

    return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
