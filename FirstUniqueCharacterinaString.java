public class Solution {
    public int firstUniqChar(String s) {
        int[] dic = new int[26];
        for(char c:s.toCharArray())
            dic[c-'a'] ++;
        for(int i=0;i<s.length();i++)
            if(dic[s.charAt(i)-'a'] == 1)
                return i;
        return -1;
    }
}