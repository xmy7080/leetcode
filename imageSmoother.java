class Solution {
    int m = 0;
    int n = 0;

    public int[][] imageSmoother(int[][] img) {
        m = img.length;
        n = img[0].length;
        int[][] result = new int[m][n];
        for(int i = 0; i< m; i++)
            for(int j = 0; j < n; j++){
                result[i][j] = aroundSum(i, j, img);
            }
        return result;
    }

    private int aroundSum(int x, int y, int[][] img){
        int result = 0;
        int count = 0;
        for(int i = x-1; i< x+2;i++){
            if(i <0 || i >=m) continue;
            for(int j = y-1; j< y+2;j++){
                if(j <0 || j >=n) continue;
                count ++;
                result += img[i][j];
            }
        }
        return (int) Math.floor(result/count);
    }
}
