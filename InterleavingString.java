public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length(), l2 = s2.length(), l3 = s3.length();
        if(l1 + l2 != l3) return false;
        boolean[][] matrix = new boolean[l1+1][l2+1];
        matrix[0][0] = true;
        for(int i = 0;i<=l1;i++)
            for(int j = 0;j<=l2;j++){//i,j stands for idx in matrix, matrix[i][j] matches s1[i-1], s2[j-1] and s3[i+j-1]
                if(i==0 && j==0) continue;
                matrix[i][j] = i>0 && matrix[i-1][j] && s1.charAt(i-1) == s3.charAt(i+j-1)
                            || j>0 && matrix[i][j-1] && s2.charAt(j-1) == s3.charAt(i+j-1);
                
            }
        return matrix[l1][l2];
    }
}