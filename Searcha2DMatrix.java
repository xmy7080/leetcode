public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        if(row == 0) return false;
        int col = matrix[0].length;
        int rowl = 0, rowr = row-1;//search in rows first
        int searchRow = 0, mid = 0;
        while(rowl <= rowr){
            mid = (rowl + rowr)/2;
            if (matrix[mid][0] > target){
                rowr = mid-1;
            }
            else if (matrix[mid][0] < target){
                if (mid+1<row && matrix[mid+1][0] > target){
                    
                    break;
                }
                rowl = mid+1;
                    
            }
            else{//matrix[mid][0] == target
                return true;
            }
        }
        searchRow = mid;
        int coll = 0, colr = col-1;
        while(coll <= colr){
            mid = (coll + colr)/2;
            if(matrix[searchRow][mid] < target){
                coll = mid+1;
            }
            else if(matrix[searchRow][mid] > target){
                colr = mid-1;
            }
            else//==
                return true;
        }
        return false;
    }
}