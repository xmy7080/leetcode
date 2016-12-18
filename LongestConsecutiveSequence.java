public class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 0;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int n: nums){
            if(!map.containsKey(n)){
                int left = map.containsKey(n-1)? map.get(n-1):0;
                int right = map.containsKey(n+1)? map.get(n+1):0;
                
                int span = right+left+1;
                
                map.put(n,span);
                res = Math.max(res,span);
                
                map.put(n-left,span);
                map.put(n+right,span);
            }
        }
        return res;
    }
}