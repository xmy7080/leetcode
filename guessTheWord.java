//this is a very inspiring solution, I used this but still get 1 test cases unpassed. will pass it for now
// https://leetcode.com/problems/guess-the-word/solutions/711901/java-solution-easy-to-understand/?envType=company&envId=verkada&favoriteSlug=verkada-more-than-six-months
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }
 */
class Solution {
    HashMap<String, Integer> map = new HashMap<>();
    public void findSecretWord(String[] words, Master master) {
        // build the similarity map, count how many other words each word matches with
        // (at least 1 position)
        for(int i = 0; i< words.length -1;i++)
            for(int j = i+1; j <words.length;j++){
                String word1 = words[i];
                String word2 = words[j];

                if(compare(word1, word2) > 0){
                    map.put(word1, map.getOrDefault(word1, 0) + 1);
                    map.put(word2, map.getOrDefault(word2, 0) + 1);
                }
            }
        
        Arrays.sort(words, (a, b) -> map.getOrDefault(b, 0) - map.getOrDefault(a, 0));
        for(int i = 0; i < words.length;i ++){
            String guess = words[i];
            if(guess.isEmpty()) continue;
            int matchedCount = master.guess(guess);

            if(matchedCount == 6) break;
            
            filterOut(guess, words, i+1, matchedCount);
        }
    }
    void filterOut(String guess, String[] words, int start, int matchedCount) {
        for(int i= start; i< words.length; i++){
            if(words[i].isEmpty()) continue;
            if(compare(words[i], guess) != matchedCount){
                words[i] = "";
            }
        }
    }

    int compare(String a, String b) {
        int res = 0;
        for(int i = 0;i< a.length(); i++){
            if(a.charAt(i) == b.charAt(i) ) res ++;
        }
        return res;
    }
}
