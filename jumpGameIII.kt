class Solution {
    fun canReach(arr: IntArray, start: Int): Boolean {
        val visited = BooleanArray(arr.size)
        val queue = ArrayDeque<Int>()
        visited[start] = true
        queue.addLast(start)
        while (queue.isNotEmpty()){
            val curr = queue.removeFirst()
            if (arr[curr] == 0) return true
            for (i in listOf(curr + arr[curr], curr - arr[curr])){
                if (i >= 0 && i < arr.size && !visited[i]){
                    queue.addLast(i)
                    visited[i] = true
                }
            }
        }
        return false
    }
}
