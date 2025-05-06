class WordDistance(wordsDict: Array<String>) {
    val map = hashMapOf<String, List<Int>>()
    init{
        for(i in 0 until wordsDict.size){
            val list = map.getOrDefault(wordsDict[i], listOf()).toMutableList()
            list.add(i)
            map[wordsDict[i]] = list.toList()
        }
    }

    fun shortest(word1: String, word2: String): Int {
        val list1 = map[word1]?: listOf()
        val list2 = map[word2]?: listOf()
        return findClosest(list1, list2)
    }
    private fun findClosest(list1: List<Int>, list2: List<Int>): Int{
        var result = Int.MAX_VALUE
        var i = 0; var j = 0
        while(i < list1.size && j < list2.size){
            result = min(result, abs(list1[i] - list2[j]))
            if(list1[i] > list2[j]) j++
            else i++
        }
        return result
    }

}

/**
 * Your WordDistance object will be instantiated and called as such:
 * var obj = WordDistance(wordsDict)
 * var param_1 = obj.shortest(word1,word2)
 */
