class Solution {
    fun longestPalindrome(s: String): String {
        var l = 0 // left bound inclusive
        var r = 1 // right bound inclusive
        var result = 0
        for(i in 0 until s.length){
            // single seed
            var j = i -1
            var k = i +1
            while(j >= 0 && k < s.length && s[j] == s[k]){
                j --
                k ++
            }
            if(k-1-j > result) {
                result = k-1-j
                l = j+1
                r = k-1
            }
            j = i
            k = i+1
            while(j >= 0 && k < s.length && s[j] == s[k]){
                j --
                k ++
            }
            if(k-1-j > result) {
                result = k-1-j
                l = j+1
                r = k-1
            }
        }
        return s.substring(l, r+1)
    }
}
