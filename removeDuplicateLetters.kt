// solution not from editorial, but from https://leetcode.com/problems/remove-duplicate-letters/solutions/76768/a-short-o-n-recursive-greedy-solution/

class Solution {
    fun removeDuplicateLetters(s: String): String {
        if(s.length == 0) return ""
        var count = IntArray(26)
        var position = 0 // position for the lowest lexico char that has all the uniq char to the right of it
        for (c in s){
            // println(c.toString() +" 's int is " + (c-'a').toString() + " string is " + s)
            count[c - 'a']++
        }
        for (i in s.indices){
            if (s[i] < s[position]) position = i
            if(--count[s[i] - 'a'] == 0) break
        }
        return s[position] + removeDuplicateLetters(s.substring(position).replace(""+s[position],""))
    }
}
