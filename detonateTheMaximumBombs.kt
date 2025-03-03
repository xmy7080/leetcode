// be aware of the integer overflow issue
// the count of chain reaction can be done in dfs/bfs or any other algorithm
class Solution {
    fun maximumDetonation(bombs: Array<IntArray>): Int {
        val graph = HashMap<Int, MutableList<Int>>()
        val size = bombs.size
        fun canDetonate(i: Int, j: Int): Boolean{
            val distance: Long = (bombs[i][0] - bombs[j][0]).toLong() * (bombs[i][0] - bombs[j][0]).toLong() +
            (bombs[i][1] - bombs[j][1]).toLong() * (bombs[i][1] - bombs[j][1]).toLong()
            return distance <= (bombs[i][2].toLong() * bombs[i][2].toLong())
        }
        for(i in 0 until size){
            graph[i] = mutableListOf()
        }
        for(i in 0 until size)
            for(j in 0 until size){
                if(i == j) continue
                // if i can detonate j
                if(canDetonate(i, j)){
                    val list = graph[i]!!
                    list.add(j)
                }
            }
        var maxNum = 0
        var visited = mutableSetOf<Int>()
        var count = 0
        fun dfs(start: Int) {
            visited.add(start)
            count ++
            if(graph[start] == null) return
            for(next in graph[start]!!){
                if(next !in visited){
                    dfs(next)
                }
            }
        }
        graph.forEach{ key, value ->
            count = 0
            visited = mutableSetOf<Int>()
            dfs(key)
            maxNum = if(count > maxNum) count else maxNum
        }
        return maxNum
    }
}
