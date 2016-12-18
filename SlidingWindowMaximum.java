public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums.length == 0 && k == 0)
            return new int[0];
        int n = nums.length;
        int[] res = new int[n-k+1];//result array
        int ki = 0;
        Deque<Integer> q = new ArrayDeque<Integer>();//deque that store the increasing sequence
        for(int i = 0;i<nums.length;i++){
            while(!q.isEmpty() && q.peek()< i - k + 1)
                q.poll();//remove the item that are no longer in bucket k
            while(!q.isEmpty() && nums[q.peekLast()] < nums[i])
                q.pollLast();
            q.offer(i);
            if(i>=k-1)
                res[ki++] = nums[q.peek()];
        }
        return res;
    }
}