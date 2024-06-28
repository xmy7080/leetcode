class Solution {
    fun permuteUnique(nums: IntArray): List<List<Int>> {
        val temp = mutableListOf<Int>()
        val res = mutableListOf<List<Int>>()
        val picked = hashMapOf<Int, Int>()
        for (num in nums){
            picked[num] = picked.getOrDefault(num, 0) + 1
        }
        dfs(nums, temp, picked, res)
        return res.toList()
    }

    fun dfs(nums: IntArray, temp: MutableList<Int>, picked: HashMap<Int, Int>, res: MutableList<List<Int>>) {
        if (temp.size == nums.size) {
            res.add(temp.toList())
            return
        }
        for ((num, count) in picked){
            if (count > 0){
                picked[num] = picked[num]!! - 1
                temp.add(num)
                dfs(nums, temp, picked, res)
                temp.removeAt(temp.size -1) // remove from the last position
                picked[num] = picked[num]!! + 1
            }
        }
    }
}
