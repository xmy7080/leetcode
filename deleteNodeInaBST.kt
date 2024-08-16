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
class Solution {
    fun successor(root: TreeNode): Int {
        var node = root.right
        while(node.left != null){
            node = node.left
        }
        return node.`val`
    }
    fun predecessor(root: TreeNode): Int {
        var node = root.left
        while(node.right != null){
            node = node.right
        }
        return node.`val`
    }
    fun deleteNode(nonAlterRoot: TreeNode?, key: Int): TreeNode? {
        var root = nonAlterRoot
        if (root != null){
            if (root.`val` < key) root.right = deleteNode(root.right, key)
            else if (root.`val` > key) root.left = deleteNode(root.left, key)
            else {// root.val == key, need remove the curr node
                if (root.left == null && root.right == null) root = null
                else if (root.left != null) {
                    root.`val` = predecessor(root)
                    root.left = deleteNode(root.left, root.`val`)
                } else {
                    root.`val` = successor(root)
                    root.right = deleteNode(root.right, root.`val`)
                }
            }
        }
        return root
    }
    // unsuccessful try with iterative approach, finding its predecessor and successor
    // fun deleteNode(root: TreeNode?, key: Int): TreeNode? {
    //     val stk = ArrayDeque<TreeNode>()
    //     var found: TreeNode? = null
    //     var father: TreeNode? = null
    //     var curr = root
    //     while (stk.isNotEmpty() || curr != null){
    //         while (curr != null){
    //             stk.addFirst(curr!!)
    //             curr = curr!!.left
    //         }
    //         if (!found) father = curr
    //         curr = stk.removeFirst()
    //         if (found != null) {
    //             // at the moment, found is the one to be removed, curr is the successor
    //             if (father != null) {
    //                 if (father.left != null && father.left.`val` == key) father.left = curr
    //                 if (father.right != null && father.right.`val` == key) father.right = curr
    //             }
    //             curr.left = found.left
    //             curr.right = found.right
    //         }
    //         if (curr.`val` == key) found = curr
    //         curr = curr.right

    //     }
    // }
}
