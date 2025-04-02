/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int = 0) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        return findLCA(root, p, q)
    }
    fun findLCA(node: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode?{
        // if found one node match p or q, return it
        if(node == null || node == p || node == q) return root
        val left = findLCA(node.left, p, q)
        val right = findLCA(node.right, p, q)
        // if left and right both not null, the current node is the LCA
        // if only one side returned not null, return that not null side
        return if(left != null && right != null) node else left ?: right
    }

    // old version solution that are easy to understand
    // Stores the value of node p from the input.
    var pT: Int? = null

    // Stores the value of node q from the input.
    var qT: Int? = null

    // Stores the path from the root to node p as a list of node values.
    var pList = listOf<Int>()

    // Stores the path from the root to node q as a list of node values.
    var qList = listOf<Int>()

    // Stores the result (the lowest common ancestor) as an integer value.
    var result: Int? = null

    // Finds the lowest common ancestor of nodes p and q in a binary tree.
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        // Assign the values of nodes p and q.
        pT = p!!.`val`
        qT = q!!.`val`
        // Temporary list to track the current path during traversal.
        var tmp = mutableListOf<Int>()


        // Traverse the tree and record the paths to p and q.
        helper(root!!, tmp)

        // Compare the paths to find the last common node (lowest common ancestor).
        for (idx in 0 until pList.size) {
            if (idx < qList.size && qList[idx] == pList[idx]) {
                // Update the result if the nodes in both paths match.
                result = pList[idx]
                continue
            } else if (idx >= qList.size || qList[idx] != pList[idx]) {
                // Break when paths start to diverge.
                break
            }
        }

        // If result is null, return a default TreeNode with value 0.
        return TreeNode(result ?: 0)
    }

    // Helper method to perform Depth-First Search (DFS) to record paths to p and q.
    fun helper(node: TreeNode, tmp: MutableList<Int>) {
        // Add the current node's value to the path.
        tmp.add(node.`val`)

        // Record the path if the current node's value matches pT.
        if (node.`val` == pT) pList = tmp.toList()

        // Record the path if the current node's value matches qT.
        if (node.`val` == qT) qList = tmp.toList()

        // Recursively traverse the left subtree, if it exists.
        if (node.left != null) helper(node.left!!, tmp)

        // Recursively traverse the right subtree, if it exists.
        if (node.right != null) helper(node.right!!, tmp)

        // Backtrack by removing the last added node value.
        tmp.removeLast()

        return
    }
}
