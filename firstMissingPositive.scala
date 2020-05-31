//details https://leetcode.com/articles/first-missing-positive/
//dustin's scala solution   https://leetcode.com/problems/first-missing-positive/discuss/392546/Scala-solution
//no need to convert any > n ele to 1, during the flip sign process, we can just flip the idx that are within the num length, see line 17
object Solution {
    def firstMissingPositive(nums: Array[Int]): Int = {
        val hasOne = nums.indices.foldLeft(false)((hasOne, idx) =>
            if(nums(idx) < 1){
                nums(idx) = 1
                hasOne
            }
            else hasOne || nums(idx) == 1
        )
        if (!hasOne) 1
        else{
            nums.indices.foreach(idx =>{
                val positiveVal: Int = Math.abs(nums(idx) )
                if (positiveVal - 1 < nums.length){
                    nums(positiveVal -1) = -1 * Math.abs(nums(positiveVal -1) )
                }
            })
            
            nums.indices.find(idx => nums(idx) > 0).map(_ + 1).getOrElse(nums.length + 1)
        }
    }
}
