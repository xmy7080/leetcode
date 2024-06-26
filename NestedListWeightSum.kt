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
    fun depthSum(nestedList: List<NestedInteger>): Int {
        return helper(1, nestedList)
    }

    fun helper(level: Int, nestedList: List<NestedInteger>?): Int {
        if (nestedList == null) return 0
        var levelSum = 0
        nestedList!!.forEach {
            if (it.isInteger()){
                levelSum += it.getInteger() * level
            } else {
                levelSum += helper(level + 1, it.getList())
            }
        }
        return levelSum
    }
}
