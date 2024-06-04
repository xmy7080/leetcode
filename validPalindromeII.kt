class Solution {
    fun isPalindrome(s: String): Boolean {
        var l = 0
        var r = s.length -1
        do {
            if (s[l] != s[r]) return false
            l++
            r--
        } while (l < r)
        return true
    }

    fun validPalindrome(s: String): Boolean {
        var l = 0
        var r = s.length -1
        do {
            // check either substring l to r-1 and l+1 to r is palindrome
            if (s[l] != s[r]) return isPalindrome(s.substring(l, r)) || isPalindrome(s.substring(l+1, r+1))
            l++
            r--
        } while (l < r)
        return true
    }
}
