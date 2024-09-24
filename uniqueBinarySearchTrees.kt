//dfs with memoization approach
class Solution {
    fun numTrees(n: Int): Int {
        var counts = IntArray(n+1){0}
        counts[0] = 1
        counts[1] = 1
        fun dfs(size: Int): Int {
            // if(size == 1 || size == 0) return 1
            if(counts[size] != 0) return counts[size]
            var temp = 0
            for(i in 0 .. size-1){
                temp += dfs(i) * dfs(size - 1 - i)
            }
            counts[size] = temp
            return temp
        }
        return dfs(n)
    }
}
