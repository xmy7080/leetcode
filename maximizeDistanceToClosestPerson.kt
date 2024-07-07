class Solution {
    fun maxDistToClosest(seats: IntArray): Int {
        var distance = 0
        var lastPersonIdx = -1

        var startDistance = 0
        for (i in 0 until seats.size){
            val occupied = seats[i]
            if (occupied == 1 && lastPersonIdx == -1){ // when first saw a person, say it sits at 2, then distance from beginning to it is 2
                lastPersonIdx = i
                startDistance = i
            }
            else if ( occupied == 1 && lastPersonIdx != -1){ // saw two person at least, update distance if they sits further than 1
                if ((i - lastPersonIdx) > 1) {
                    val tempIdx = (i + lastPersonIdx)/2
                    val tempDistance = tempIdx - lastPersonIdx
                    if (distance < tempDistance){
                        distance = tempDistance
                    }
                }
                lastPersonIdx = i // no matter the two person's sits distance, we need update the last person
            }
        }
        val endDistance = seats.size - lastPersonIdx - 1 // the case when there are empty seats at the end
        distance = maxOf(startDistance, endDistance, distance)
        return distance
    }
}
