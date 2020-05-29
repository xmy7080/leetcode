object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    //dustin's solution
        def twoSum(idx: Int, prev: Map[Int, Int]): Array[Int] = {
            prev.get(target - nums(idx)) match {
                case Some(idx0) => Array(idx0, idx)
                case None => twoSum(idx + 1, prev + (nums(idx) -> idx) )
            }
        }
        twoSum(0, Map.empty)
        //another solution with foldleft
        // nums.zipWithIndex.foldLeft(Map.empty[Int, Int] )((m, x) =>
        //     {
        //         m.get(target - x._1) match {
        //             case Some(idx) => return Array(idx, x._2)
        //             case None => m ++ Map(x._1 -> x._2)
        //         }
        //     })
        // Array.empty
    }
}
