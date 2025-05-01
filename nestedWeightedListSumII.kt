//a better solution from another leetcoder
// this basically recalculate the base level one more time when we go one more level up. Better time and space complexity 
fun depthSumInverse(nestedList: List<NestedInteger>): Int {
    var total = 0; var levelSum = 0;
    var q = LinkedHashSet<NestedInteger>(nestedList);
    while(!q.isEmpty()) {
        var count = q.size;
        while(count-- > 0) {
            val cur = q.first();
            q.remove(q.first());
            if (cur.isInteger()) levelSum += cur.getInteger();
            else q.addAll(cur.getList());
        }
        total += levelSum;
    }
    return total;
}

// my original solution
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     constructor()
 *
 *     // Constructor initializes a single integer.
 *     constructor(value: Int)
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     fun isInteger(): Boolean
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     fun getInteger(): Int?
 *
 *     // Set this NestedInteger to hold a single integer.
 *     fun setInteger(value: Int): Unit
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     fun add(ni: NestedInteger): Unit
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     fun getList(): List<NestedInteger>?
 * }
 */
class Solution {
    fun depthSumInverse(nestedList: List<NestedInteger>): Int {
        var depth = 1
        var maxDeep = 1
        var total = 0

        fun dfsCountMaxDeep(nesteds: List<NestedInteger>) {
            depth += 1
            maxDeep = intArrayOf(maxDeep, depth).max()
            for(nested in nesteds){
                if(!nested.isInteger()){
                    dfsCountMaxDeep(nested.getList())
                }
            }
            depth -= 1
        }
        fun dfsCalculateTotal(ni : NestedInteger) {
            if(ni.isInteger()){
                total += (maxDeep - depth + 1) * ni.getInteger()
            } else{
                depth ++
                for(nestInt in ni.getList()){
                    dfsCalculateTotal(nestInt)
                }
                depth --
            }
        }
        for(nested in nestedList){
            if(!nested.isInteger())
                dfsCountMaxDeep(nested.getList())
        }
        for(nested in nestedList){
            dfsCalculateTotal(nested)
        }
        return total
    }
}
