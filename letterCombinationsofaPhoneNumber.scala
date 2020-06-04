#https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8079/scala-tail-rec
#very neat way of mimicing how python dealing with this.
object Solution {
    val m = Map(('2' -> "abc"), ('3' -> "def"), ('4' -> "ghi"), ('5'-> "jkl"), ('6' -> "mno"), ('7' -> "pqrs"), ('8' -> "tuv"), ('9' -> "wxyz")).mapValues(_.toList)
    def letterCombinations(digits: String): List[String] = {
        def rec(digits: String, acc: List[String]): List[String] = {
            if (digits == "") acc
            else rec(digits.tail, acc.flatMap(x => m(digits.head).map(y => x+y)))
        }
        if (digits == "")
            List()
        else
            rec(digits, List(""))
    }
}
