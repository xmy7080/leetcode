//https://leetcode.com/problems/non-overlapping-intervals/editorial/
//
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> a[1]- b[1]);
        int result = 0;
        int k = Integer.MIN_VALUE;
        for(int[] interval : intervals){
            int x = interval[0];
            int y = interval[1];
            if(x >= k){
                result ++;
                k = y;
            }
        }
        return intervals.length - result;
    }
}
