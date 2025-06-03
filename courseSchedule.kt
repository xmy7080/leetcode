// graph khan algorithm solution, refer to editorial approach #1
class Solution {
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        var indegree = IntArray(numCourses) {0}
        val adj = List<MutableList<Int>>(numCourses) {mutableListOf<Int>()}

        for(direct in prerequisites){
            indegree[direct[0]]++
            adj[direct[1]].add(direct[0])
        }

        val queue = ArrayDeque<Int>()
        for(i in 0 until numCourses){
            if(indegree[i] ==0)
                queue.addLast(i)
        }

        var visitedCount = 0
        while(queue.isNotEmpty()){
            val curr = queue.removeFirst()
            visitedCount ++
            for(next in adj[curr]){
                indegree[next] --
                if(indegree[next] == 0)
                    queue.addLast(next)
            }
        }

        return visitedCount == numCourses
    }
}
// dfs cycle detection solution, editorial approach #2
class Solution {
    fun dfs(curr: Int, visited: BooleanArray, inStack: BooleanArray, nextMap: HashMap<Int, MutableList<Int>>): Boolean{
        if(inStack[curr]) return true
        if(visited[curr]) return false
        
        visited[curr] = true
        inStack[curr] = true

        for(next in nextMap.getOrDefault(curr, mutableListOf<Int>())){
            if(dfs(next, visited, inStack, nextMap)){
                return true
            }
        }
        inStack[curr] = false
        return false
    }
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val nextMap = HashMap<Int, MutableList<Int>>()
        val visited = BooleanArray(numCourses){false}
        val inStack = BooleanArray(numCourses){false}

        for(array in prerequisites){
            val list = nextMap.getOrPut(array[1]) {mutableListOf<Int>()}
            list.add(array[0])
        }
        for(i in 0 until numCourses){
            if(dfs(i, visited, inStack, nextMap)){
                return false
            }
        }
        return true
    }
}
