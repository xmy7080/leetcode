class Solution {
    fun lengthOfLongestSubstringKDistinct(s: String, k: Int): Int {
        val group = HashMap<Char, Int>()
        var l = 0
        var r = 0
        var res = 0
        while (r < s.length && l < s.length) {
            while (r < s.length) {
                if (group.size == k && s[r] !in group) break
                val count = group[s[r]] ?: 0
                group[s[r]] = count + 1
                // println(s[r] +" " + group[s[r]]!!)
                r ++
            }
            // var groupL = group.map { it.key.toString() + '-' + it.value }
            // println(groupL + "r: " + r + "l: " + l)
            res = maxOf(res, r - l)
            val count = group[s[l]] ?: 0
            group[s[l]] = count - 1
            if (count -1 <= 0) group.remove(s[l])
            l ++
        }
        return res
    }
}
