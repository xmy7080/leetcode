/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var neighbors: ArrayList<Node?> = ArrayList<Node?>()
 * }
 */

class Solution {
    fun cloneGraph(node: Node?): Node? {
        if(node == null) return node
        val map = HashMap<Node, Node>()
        val queue = ArrayDeque<Node>()
        map[node!!] = Node(node!!.`val`)
        queue.addLast(node!!)
        while(queue.isNotEmpty()){
            val curr = queue.removeFirst()
            // map[curr] = Node(curr.`val`) // this line is wrong, as it will flush any node that already cloned and added to neighbors
            curr.neighbors.forEach{it ->
                if(it != null){
                    if(it !in map){
                        val newNode = Node(it.`val`)
                        map[it!!] = newNode
                        queue.addLast(it)
                    }
                    map[curr]!!.neighbors.add(map[it])
                    // map[it]!!.neighbors.add(map[curr]) // we don't need a reverse add because every new node will be traversed for at least once
                }
            }
        }
        return map[node!!]
    }
}
