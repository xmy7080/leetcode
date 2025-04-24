// java solution
class Solution {
    // private boolean overlap(int[] a, int[] b){
    //     return !(a[0] > b[1] || a[1] < b[0]);
    // }
    // private int[] combine(int[] a, int[] b){
    //     return int[] {min(a[0], b[0]), max(a[1], b[1])};
    // }
    public int[][] merge(int[][] intervals) {
        if(intervals.length <= 1) return intervals;
        Arrays.sort(intervals, Comparator.comparingInt(i -> i[0]));
        List<int[]> res = new ArrayList<>();
        int[] newInterval = intervals[0];
        for(int[] itv: intervals){
            if(itv[0] <= newInterval[1]){
                newInterval[1] = Math.max(itv[1], newInterval[1]);
            } else{
                res.add(newInterval);
                newInterval = itv;
            }
        }
        res.add(newInterval);
        return res.toArray(new int[res.size()][]);
    }
}
