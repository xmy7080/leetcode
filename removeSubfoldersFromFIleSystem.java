//editorial solution
//https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/editorial/?envType=company&envId=verkada&favoriteSlug=verkada-all
class Solution {
    static class Trie {
        boolean isFolderEnd;
        HashMap<String, Trie> children;
        public Trie(){
            this.isFolderEnd = false;
            this.children = new HashMap<String, Trie>();
        }
    }
    Trie root;
    Solution(){
        this.root = new Trie();
    }
    public List<String> removeSubfolders(String[] folder) {
        for(String path : folder){
            Trie node = root;
            String[] names = path.split("/");
            for(String name: names){
                
                if(!node.children.containsKey(name) ){
                    node.children.put(name, new Trie());
                }
                node = node.children.get(name);
            }
            node.isFolderEnd = true;
        }
        List<String> result = new ArrayList<String>();
        for(String path: folder){
            Trie node = root;
            String[] names = path.split("/");
            boolean isSubFolder = false;

            for(int i=0;i<names.length;i++){
                node = node.children.get(names[i]);
                if(node.isFolderEnd && i != names.length-1){
                    isSubFolder = true;
                    break;
                }
            }
            if(!isSubFolder) result.add(path);
        }
        return result;
    }
}
