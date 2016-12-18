public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] isword = new boolean[s.length()+1];
        isword[0] = true;
        int maxl = 0;
        for(String str: wordDict){
            maxl = Math.max(maxl, str.length());
        }
        
        for(int i = 1;i<=s.length();i++){
            //i is idx for isword, which indicate if s[i-1] can form a word
            for(int j = i-1;j>=0 && j>=i-maxl && !isword[i]; j--){
                String substr = s.substring(j,i);
                if(isword[j] && wordDict.contains(substr)){
                    isword[i] = true;
                }
            }
        }
        return isword[s.length()];
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        //         :type s: str
        // :type wordDict: Set[str]
        // :rtype: bool
        // """
        // if not s: return True
        // if not wordDict: return False
        // isword = [False] * (len(s)+1)
        // isword[0] = True
        
        // maxl = 0
        // for w in wordDict:
        //     maxl = max(maxl,len(w))
        // for i in xrange(len(s)+1):
        //     j = i-1
        //     while j>= i-maxl and j>=0:
        //         if isword[j] and s[j:i] in wordDict:
        //             isword[i] = True
        //             break
        //         j -= 1
        // return isword[len(s)]
    }
}