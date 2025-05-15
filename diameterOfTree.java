/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int result = 0;
    public int diameterOfBinaryTree(TreeNode root) {

        dfs(root);
        return result;
    }
    private int dfs(TreeNode node){
        int left = node.left != null ? dfs(node.left) : 0;
        int right = node.right != null ? dfs(node.right) : 0;
        // System.out.println("node val is " + node.val + " left is " + left + " right is " + right  );
        result = Math.max(result, left + right);
        return left > right ? left+1: right+1;
    }
}
