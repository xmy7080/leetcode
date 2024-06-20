class Solution {
    fun canCross(stones: IntArray): Boolean {
        val stoneWithSteps = HashMap<Int, MutableSet<Int>>() // stores the distance of the stone as key, the multiple last jump steps can reach to this stone as value, eg 5 -> [2,3] means frog can jump to 5 with either 2 or 3 as last steps
        stones.forEach { value ->
            stoneWithSteps.put(value, mutableSetOf<Int>())
        }
        stoneWithSteps.put(stones.first(), mutableSetOf(0))
        stones.forEach{value ->
            val steps = stoneWithSteps.get(value)!!
            // print("stones "+ value + " steps " + steps.toString() + "\n")
            for (step in steps) {
                for (delta in -1 .. 1) {
                    val nextStep = step + delta
                    if (nextStep + value in stoneWithSteps) {
                        stoneWithSteps.get(nextStep + value)!!.add(nextStep)
                    }
                }
            }
        }
        return stoneWithSteps.get(stones.last())!!.isNotEmpty()
    }
}
