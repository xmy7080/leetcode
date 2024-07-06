// kotlin solution https://leetcode.com/problems/number-of-islands-ii/solutions/5057718/kotlin-union-find/
// leetcode union find tutorial https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3879/

class UnionSet(val size: Int) {
    val parents = IntArray(size) {it}
    val rank = IntArray(size)

    fun find(x: Int): Int {
        if (parents[x] != x){
            parents[x] = find(parents[x])
        }
        return parents[x]
    }

    fun union(x: Int, y: Int): Boolean{
        val rootX = find(x)
        val rootY = find(y)
        if (rootX == rootY) return false

        val rankX = rank[rootX]
        val rankY = rank[rootY]
        if (rankX > rankY){
            parents[rootY] = parents[rootX]
        } else if (rankX < rankY) {
            parents[rootX] = parents[rootY] 
        } else {
            rank[rootY] ++
            parents[rootX] = parents[rootY] 
        }
        return true
    }
}
val DIRECTIONS = arrayOf(Pair(1, 0), Pair(0, 1), Pair(-1, 0), Pair(0, -1))

class Solution {
    fun numIslands2(m: Int, n: Int, positions: Array<IntArray>): List<Int> {
        val result = mutableListOf<Int>()
        val unionSet = UnionSet(m * n)
        val grid: Array<IntArray> = Array(m) {IntArray(n) {0}}
        var islands = 0
        for ((r, c) in positions){
            val number = r * n + c
            if (grid[r][c] == 1){
                result.add(islands)
                continue
            }
            grid[r][c] = 1
            islands ++

            for((x, y) in DIRECTIONS){
                val nr = r + x
                val nc = c + y
                val neighbor = nr * n + nc
                if ( (nr in 0 until m) && (nc in 0 until n) && grid[nr][nc] == 1 ){
                    if (unionSet.union(number, neighbor)){
                        islands --
                    }
                }
            }
            result.add(islands)
        }
        return result
    }
}
