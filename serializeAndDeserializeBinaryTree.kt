// used the default in order traversal
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Codec() {
	// Encodes a URL to a shortened URL.
    fun serialize(root: TreeNode?): String {
        val sb = StringBuilder("")
        fun serializeHelper(node: TreeNode?) {
            if(node == null) sb.append("null,")
            else {
                sb.append(node!!.`val`.toString() + ",")
                serializeHelper(node!!.left)
                serializeHelper(node!!.right)
            }
        }
        serializeHelper(root)
        return sb.toString()
    }

    // Decodes your encoded data to tree.
    fun deserialize(data: String): TreeNode? {
        val queue = ArrayDeque(data.split(","))
        fun deserializeHelper(): TreeNode?{
            val rootStr = queue.removeFirst()
            if(rootStr == "null"){
                return null
            } else{
                val root = TreeNode(rootStr.toInt())
                root.left = deserializeHelper()
                root.right = deserializeHelper()
                return root
            }
        }
        return deserializeHelper()
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var ser = Codec()
 * var deser = Codec()
 * var data = ser.serialize(longUrl)
 * var ans = deser.deserialize(data)
 */
