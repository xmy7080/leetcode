/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void recoverTree(TreeNode root) {
        if(root==null) return;
        List<TreeNode> record = new ArrayList<TreeNode>(2);
        helper(root, record, new ArrayList<TreeNode>());
        int tmp = record.get(0).val;
        record.get(0).val = record.get(1).val;
        record.get(1).val = tmp;
    }
    
    public void helper(TreeNode root, List<TreeNode> record, List<TreeNode> cur){
        if(root==null) return;
        helper(root.left, record, cur);
        if(cur.size()==0) cur.add(root);
        else if(cur.get(0).val>root.val){
            if(record.size()==0){
                record.add(cur.get(0));
                record.add(root);
            }else record.set(1, root);
        }
        cur.set(0, root);
        helper(root.right, record, cur);
    }
}