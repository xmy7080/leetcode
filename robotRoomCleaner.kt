// used the editorial solution
// right hand rules https://en.wikipedia.org/wiki/Maze-solving_algorithm#Wall_follower
/**
 * // This is the Robot's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     fun move(): Boolean {}
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     fun turnLeft() {}
 *     fun turnRight() {}
 *
 *     // Clean the current cell.
 *     fun clean() {}
 * }
 */

class Solution {
    val dirs = arrayOf(-1 to 0, 0 to 1, 1 to 0, 0 to -1)
    val visited = mutableSetOf<Pair<Int, Int>>()
    lateinit var robot: Robot
    fun goBack() { // after forward cell traverse done, go back to its previous state prior the move forward
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
    }
    fun backtrack(row: Int, col: Int, initialDirection: Int) {
        robot.clean()
        visited.add(row to col)

        // go in four directions up, right, down and left
        for(i in 0 until 4){
            val newDir = (initialDirection + i) % 4
            val newRow = row + dirs[newDir].first
            val newCol = col + dirs[newDir].second

            if((newRow to newCol) !in visited && robot.move()){
                backtrack(newRow, newCol, newDir)
                goBack()
            }
            robot.turnRight()
        }
    }

    fun cleanRoom(robot: Robot) {
        this.robot = robot
        backtrack(0,0,0)
    }
}
