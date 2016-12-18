public class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        // if(matrix.length == 0)
        int m = matrix.length, n = matrix[0].length;
        PriorityQueue<int[]> que = new PriorityQueue<int[]>((a,b)-> a[0] - b[0] );
        for(int i=0;i<m && i<k;i++) que.offer(new int[]{matrix[i][0],i,0});//save as {value, i, j}
        while(k-->1 && !que.isEmpty() ){
            int[] tmp = que.poll();
            if(tmp[2]+1 < n)
                que.offer(new int[]{matrix[tmp[1]][tmp[2]+1], tmp[1],tmp[2]+1} );
        }
        return que.poll()[0];
    }
}