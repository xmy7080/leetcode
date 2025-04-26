class Solution {
    public int[][] transpose(int[][] matrix) {
        // transpose for non-square matrix
        int row = matrix.length;
        int col = matrix[0].length;
        int[][] res = new int[col][row];
        for(int i = 0; i < row; i++)
            for(int j = 0; j < col; j++)
                res[j][i] = matrix[i][j];
        return res;

        // in place transpose for square matrix
        // for(int i = 0; i < row; i++)
        //     for(int j = i+1; j < col; j++){
        //         int tmp = matrix[j][i];
        //         matrix[j][i] = matrix[i][j];
        //         matrix[i][j] = tmp;
        //     }
        // return matrix;
    }
}
