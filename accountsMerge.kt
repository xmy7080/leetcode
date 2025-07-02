class Union(val sz: Int){
    val represent = IntArray(sz) {it}
    val size = IntArray(sz) {1}
    // Finds the representative of group x with path compression
    fun findRepresent(num: Int): Int{
        if(represent[num] == num){
            return num
        }
        represent[num] = findRepresent(represent[num])
        return represent[num]
    }
    // Unite groups by size
    fun unionBySize(a: Int, b: Int){
        val repA = findRepresent(a)
        val repB = findRepresent(b)

        if(repA == repB){
            return
        }
        if(size[repA] >= size[repB]){
            size[repA] += size[repB]
            represent[repB] = repA
        } else {
            size[repB] += size[repA]
            represent[repA] = repB
        }
    }
}
class Solution {
    fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
        val union = Union(accounts.size)
        val emailGroup = mutableMapOf<String, Int>()

        // Build DSU based on shared emails
        for((i, account) in accounts.withIndex()){
            for(j in 1 until account.size){
                if(account[j] !in emailGroup){
                    emailGroup[account[j]] = i
                } else {
                    union.unionBySize(emailGroup[account[j]]!!, i)
                }
            }
        }

        // Map representatives to emails
        val groupToEmails = mutableMapOf<Int, MutableList<String>>()
        for((email, group) in emailGroup){
            val rep = union.findRepresent(group)
            groupToEmails.getOrPut(rep) {mutableListOf()}.add(email)
        }
        // Merge accounts with name and sorted emails
        val result = mutableListOf<List<String>>()
        for((group, emails) in groupToEmails){
            emails.sort()
            val name = accounts.get(group).get(0)
            result.add(listOf(name) + emails)
        }
        return result
    }
}
