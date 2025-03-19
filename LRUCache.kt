class LRUCache(val capacity: Int) {
    private var map = mutableMapOf<Int, LinkedNode>()
    private var firstNode = LinkedNode(-1, -1)
    private var lastNode = firstNode
    // private val capacity = capacity

    fun get(key: Int): Int {
        // val node = map[key] ?: return -1
        // delete(node)
        // append(node)
        // return node.value
        if (key in map){
            val node = map[key]
            delete(node!!)
            append(node!!)
            return node!!.value
        }
        else {
            return -1
        }
    }

    fun put(key: Int, value: Int) {
        if (key in map){
            delete(map[key]!!)
            append(LinkedNode(key, value))
        }
        else if (map.size == capacity) {
            delete(firstNode.right!!)
            append(LinkedNode(key, value))
        }
        else {
            append(LinkedNode(key, value))
        }
    }
    private fun append(node: LinkedNode) {
        lastNode.right = node
        node.left = lastNode
        lastNode = node
        map[node.key] = node
    }
    private fun delete(node: LinkedNode) {
        node.left!!.right = node.right
        node.right?.let {it.left = node.left!!}
        map -= node.key

// last node
        if(lastNode == node) {
            lastNode = node.left!!
        }

        // these two steps are necessary, not because garbage collection reason, but because we don't want dangling reference to its old neighbors.
        // for example, in line 15 16, 
        //    delete(node!!)
        //  append(node!!)
        // commenting out below will make the node.right keeps pointing to its old neighbors. as in append there are no update to the nodes.right pointer
        node.left = null
        node.right = null
    }

    private class LinkedNode(
        val key: Int,
        val value: Int,
        var left: LinkedNode? = null,
        var right: LinkedNode? = null
        )
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
