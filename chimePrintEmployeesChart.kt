/*
 *	// Definition for Employee.
 *	class Employee {
 *		var id:Int = 0
 *		var importance:Int = 0
 *		var subordinates:List<Int> = listOf()
 *	}
 */
 // use this to prepare chime interviews
// importance field will be treated as emp id who is reporting to 
/*
输入 string：“1:Bill:2, 2:John:0, 3:Jerry:2, 4:Max:1" 如果某个employee的managerid is 0， 说明他是最大的manager。
输出一个org chart：
John
- Bill
-- Max
- Jerry
*/
class Solution {
    fun getImportance(employees: List<Employee?>, id: Int): Int {
        val dict = HashMap<Int, Employee>()
        for(employee in employees){
            val currEmployee = employee!!
            dict[currEmployee.id] = currEmployee
        }
        for(employee in employees){
            val currEmployee = employee!!
            if(dict.contains(currEmployee.importance) && currEmployee.importance != currEmployee.id) {
                val whosBoss = dict[currEmployee.importance]!!
                val tmpList = whosBoss.subordinates.toMutableList()
                tmpList.add(currEmployee.id)
                whosBoss.subordinates = tmpList
            }
        }
        fun dfsPrint(currId: Int, level: Int){
            val str = " - ".repeat(level) + currId + " name unavailable"
            println(str)
            for(teammateId in dict[currId]!!.subordinates){
                dfsPrint(teammateId, level + 1)
            }
        }
        dfsPrint(id, 0)
        return 1
    }
}
// the result print will double the tree chart
// input set 1
//employees = [[1,2,[4]],[2,0,[1,3]], [3,2,[]], [4,1,[]]]
// id = 2

// input set 2
//employees = [[1,1,[2,3,77]],[3,1,[8]], [2,1,[4]], [4,2,[7]], [7,4,[]], [8,3,[9]], [9,8,[]], [77,1,[]]]
// id = 1
