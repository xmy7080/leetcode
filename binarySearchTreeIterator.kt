/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class BSTIterator(root: TreeNode?) {
    val stk = Stack<TreeNode>()
    var next: TreeNode? = null
    init{
        next = root
        while(next?.left != null){
            stk.push(next!!)
            next = next?.left
        }
    }
    fun next(): Int {
        val tmp = next!!
        if(next?.right != null){
            next = next?.right
            while(next?.left != null){
                stk.push(next!!)
                next = next?.left
            }
        }
        else if(stk.isNotEmpty())
            next = stk.pop()
        else
            next = null
        return tmp.`val`
    }

    fun hasNext(): Boolean {
        return next != null
    }

}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */
