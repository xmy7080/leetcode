class Solution {
    fun isPalindrome(s: String): Boolean {
        var l = 0
        var r = s.length -1
        do {
            while (l < r && !(s[l].isLetter() || s[l].isDigit() )) l++
            while (l < r && !(s[r].isLetter() || s[r].isDigit() )) r--
            if (l >= r) return true
            if (s[l].uppercaseChar() != s[r].uppercaseChar()) return false
            l++
            r--
        } while (l < r)
        return true
    }
}
