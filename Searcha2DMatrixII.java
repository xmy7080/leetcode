public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int col = n-1, row = 0;
        while( row < m && col >= 0){
            int cur = matrix[row][col];
            if(cur < target)//curr less than target, rule out the left part of curr row
                row ++;
            else if(cur > target)//larger than target, rule out the bellow part of curr col
                col --;
            else
                return true;
        }
        return false;
    }
}