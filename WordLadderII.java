import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class Solution {
    /**
     * Requirement:
     * all covered
     */

    /**
     * Design:
     * check the following steps.
     */
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList){
        // String start = beginWord, end = endWord;
        // result
        List<List<String>> result = new ArrayList<List<String>>();
        // a hashmap<str,set<>> to store a set of prior str for each str
        HashMap<String, HashSet<String>> visited = new HashMap<String, HashSet<String>>();
        // a hashmap<str,int> to store how far away we apart the begin
        HashMap<String,Integer> level = new HashMap<String,Integer>();
        // a queue<str> to store found but unvisited nodes
        Queue<String> queue = new LinkedList<String>();
        
        if(beginWord == null || endWord == null || beginWord.length() != endWord.length() )
            return result;
        
        HashSet<String> path = new HashSet<String>();
        visited.put(beginWord,path);
        level.put(beginWord,1);
        queue.add(beginWord);
        
        int minl = Integer.MAX_VALUE;
        
        while(!queue.isEmpty()){
            String s = queue.poll();
            char[] chs = s.toCharArray();
            for(int i=0;i<chs.length;i++){
                char old = chs[i];
                for(char c = 'a';c<='z';c++){
                    chs[i] = c;
                    String s2 = new String(chs);
                    //s2 is possible one char drift from s
                    if(wordList.contains(s2) && (!level.containsKey(s2) || 
                    (level.containsKey(s2) && level.get(s2) > level.get(s) ) ) ){
                        if(visited.containsKey(s2)){
                            visited.get(s2).add(s);
                            
                        }
                        else{
                            path = new HashSet<String>();
                            path.add(s);
                            visited.put(s2,path);
                            queue.add(s2);
                            level.put(s2, level.get(s) + 1 );
                        }
                    }
                    
                    if(s2 == endWord){
                        if(level.get(s2) < minl ){
                            minl = level.get(s2);
                        }
                    }
                        
                    
                }
                chs[i] = old;
            }
        }
        if(level.get(endWord) == null ) return result;
        
        List<String> tmp = new ArrayList<String>();
        tmp.add(endWord);
        back_trace(result, endWord, visited, tmp);
        
        return result;
    }












//     public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
//         String start = beginWord, end = endWord;
//         Set<String> dict = wordList;
//         HashMap<String, HashSet<String>> visited=new HashMap<String, HashSet<String>>();
// HashMap<String, Integer> level=new HashMap<String, Integer>();
//         LinkedList<String> queue=new LinkedList<String>();
//         List<List<String>> result=new ArrayList<List<String>>();
//         if (start==null || end==null || start.length()!=end.length())
//         {
//             return result;
//         }
//         // we also need to store the path from the start
//         HashSet<String> path=new HashSet<String>();
//         // we record the minimal length we get
//         int min_length=Integer.MAX_VALUE;
//         visited.put(start, path);
//         level.put(start, 1);
//         queue.add(start);
//         while(!queue.isEmpty())
//         {
//             String s=queue.remove();
//             char[] chars=s.toCharArray();
//             for (int i=0; i<s.length(); i++)
//             {
//                 char old=chars[i];
//                 for (char c='a'; c<='z'; c++)
//                 {
//                     chars[i]=c;
//                     String s2=new String(chars);
//                     // avoid circle
//                     // check whether it is in the dictionary
//                     // we only add the string which is further to the start
//                     if (dict.contains(s2) && (!level.containsKey(s2) || (level.containsKey(s2) && level.get(s2)>level.get(s)))){
//                         // we update the ancestor of the string
//                         if (visited.containsKey(s2)){
//                             visited.get(s2).add(s);
//                         }
//                         else{
//                             // we haven't seen this node before
//                             // thus we add it to the queue and also its ancestor
//                             path=new HashSet<String>();
//                             path.add(s);
//                             visited.put(s2, path);
//                             level.put(s2, level.get(s)+1);
//                             queue.add(s2);
//                         }
//                     }
//                     if (s2.equals(end)){
//                         // we found it
//                         // we will use back trace to found its path to start
//                         if (level.get(s)<min_length){
//                             // it is shortest path
//                             // ArrayList<String> entry=new ArrayList<String>();
//                             // entry.add(end);
//                             // result.addAll(back_trace(s, visited, entry));
//                             min_length=level.get(s)+1;
//                         }
//                         else
//                         {
//                             // ok, all the remaining path should be longer
//                             break;
//                         }
//                     }
//                 }
//                 chars[i]=old;
//             }
//         }
//         if(!visited.containsKey(end))//doesn't found any node lead to end, return blank
//             return result;
//         List<String> tmp = new ArrayList<String>();
//         tmp.add(end);
//         back_trace(result, end, visited, tmp);
        
//         return result;
//     }
    
    private void back_trace(List<List<String>> result, String node, 
            HashMap<String, HashSet<String>> visited, List<String> tmp){
                if(visited.get(node).size() <1 ){
                    List<String> newpath = new ArrayList<String>(tmp);
                    result.add(newpath);
                    return;
                }
                for(String str:visited.get(node)){
                    tmp.add(0,str);//insert into front
                    back_trace(result, str, visited, tmp);
                    tmp.remove(0);
                }
            }
            
            
            
            
            
            
            
// private ArrayList<ArrayList<String>> back_trace(String end, HashMap<String, HashSet<String>> visited, ArrayList<String> path){
//     ArrayList<ArrayList<String>> result=new ArrayList<ArrayList<String>>();
//     ArrayList<String> entry=new ArrayList<String>(path);
//     entry.add(0, end);
//     if (visited.get(end).size()<1){
//         result.add(entry);
//         return result;
//     }
//     for (String str: visited.get(end)){
//         result.addAll(back_trace(str, visited, entry));
        
//     }
//     return result;
// }

}
