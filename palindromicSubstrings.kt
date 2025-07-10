class Solution {
    fun countSubstrings(s: String): Int {
        var result = 0

        for(i in 0 until s.length){
            // single char case
            result ++
            var j = 1
            while(i+j < s.length && i -j >= 0 && s[i-j] == s[i+j]){
                result ++
                j++
            }
            var a = i
            var b = i + 1
            while(b < s.length && a >= 0 && s[a] == s[b]){
                result ++
                a --
                b ++
            }
        }
        return result
    }
}
