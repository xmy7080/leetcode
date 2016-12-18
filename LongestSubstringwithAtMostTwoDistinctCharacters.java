public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int l = 0, r = 0, maxl = 0;
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        while(r<s.length()){
            if(hm.size() <= 2 ){
                    //"" to "eceb",  "b" is in map
                char c = s.charAt(r++);
                if(hm.containsKey(c))
                    hm.put(c,hm.get(c)+1 );
                else
                    hm.put(c,1);
            }
            while(hm.size() >2 ){//"eceb" to "eb"
                char c = s.charAt(l++);
                hm.put(c,hm.get(c)-1 );
                if(hm.get(c) == 0)
                    hm.remove(c);
            }
            maxl = Math.max(maxl, r-l);
        }
        // maxl = Math.max(maxl, r-l);
        return maxl;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        // if (s.length() < 1) return 0;
        // int l = 0, r = 0, maxl = 0;
        // HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        // while(r < s.length()){
        //     if(hm.size() <= 2){//"" to "eceb"
        //         char c = s.charAt(r);
        //         hm.put(c,r);
        //         r++;
        //     }
        //     if(hm.size() > 2){
        //         int leftmost = s.length();
        //         for(int i: hm.values())
        //             leftmost = Math.min(leftmost , i);
        //         char c = s.charAt(leftmost);
        //         hm.remove(c);
        //         l = leftmost + 1;
        //     }
        //     maxl = Math.max(maxl, r-l);
        // }
        // return maxl;
    }
}