class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val group = mutableSetOf<Char>()
        var l = 0
        var r = 0
        var res = 0
        while (r < s.length) {
            while (r < s.length && s[r] !in group){
                group.add(s[r])
                r ++
            }
            res = maxOf(res, r-l)
            group.remove(s[l])
            l ++
        }
        return res
    }
}
