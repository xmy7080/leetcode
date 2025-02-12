// kotlin solution https://leetcode.com/problems/number-of-islands-ii/solutions/5057718/kotlin-union-find/
// leetcode union find tutorial https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3879/

// 2025 feb
class DisjointUnion(val size: Int){
    val parents = IntArray(size) {it}
    val rank = IntArray(size) 
    fun find(number: Int): Int {
        if(parents[number] != number){
            parents[number] = find(parents[number])
        }
        return parents[number]
    }
    fun union(node1: Int, node2: Int): Boolean {
        val root1 = find(node1)
        val root2 = find(node2)
        if(root1 == root2) return false

        val rank1 = rank[root1]
        val rank2 = rank[root2]

        if(rank1 < rank2) {
            parents[root1] = root2
        } else if(rank1 > rank2){
            parents[root2] = root1
        } else{
            parents[root1] = root2
            rank[root2] ++
        }
        return true
    }
}

class Solution {
    val dirs = setOf(0 to 1, 1 to 0, -1 to 0, 0 to -1)
    fun numIslands2(m: Int, n: Int, positions: Array<IntArray>): List<Int> {
        val res = IntArray(positions.size)
        val grid = Array(m) {IntArray(n) {0}}
        val unionSet = DisjointUnion(m*n)
        var islands = 0
        positions.forEachIndexed label@{ idx, arr  ->
            val a = arr[0]
            val b = arr[1]
            val number = a*n + b
            
            if(grid[a][b] == 1) {
                res[idx] = islands
                return@label
            }
            grid[a][b] = 1
            islands ++
            for((x, y) in dirs){
                val newx = a + x
                val newy = b + y
                if( (newx in 0 until m) && (newy in 0 until n) && grid[newx][newy] == 1 ){
                    val neighbor = newx*n + newy
                    if(unionSet.union(number, neighbor)){
                        islands --
                    }
                }
            }
            res[idx] = islands
        }
        return res.toList()
    }
}
// 2024 june
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
