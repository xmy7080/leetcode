public class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        //currect way
        PriorityQueue<int[]> que = new PriorityQueue<>((a,b)-> a[0]+a[1]-b[0]-b[1] );
        List<int[]> res = new ArrayList<int[]>();
        if(nums1.length == 0 || nums2.length == 0 || k ==0)
            return res;
        for(int i=0;i<nums1.length && i<k;i++) que.offer(new int[]{nums1[i], nums2[0], 0});
        while(k-- >0 && !que.isEmpty() ){
            int[] arr = que.poll();
            res.add(new int[]{arr[0], arr[1]} );
            if(arr[2]<nums2.length-1){
                que.offer(new int[]{arr[0], nums2[arr[2]+1], arr[2]+1} );
            }
        }
        return res;
        
    //can't be doing in two pointers, it add two length up, not times each other.
    //need to revise it into stack way
        // List<int[]> res = new ArrayList<int[]>();
        // if(nums1.length == 0 || nums2.length == 0 )
        //     return res;
        // int l = 0, r = 0;
        // int[] pair = null;
        // while(l<nums1.length && r<nums2.length && l+r < k){
        //     pair = new int[2];
        //     pair[0] = nums1[l];
        //     pair[1] = nums2[r];
        //     res.add(pair);
        //     if(l+1<nums1.length && r+1<nums2.length){
        //         if(nums1[l+1] - nums1[l] > nums2[r+1]- nums2[r]){
        //             r++;
        //         }
        //         else{
        //             l++;
        //         }
        //     }
        //     else if(l+1==nums1.length){
        //         r++;
        //     }
        //     else if(r+1== nums2.length){
        //         l++;
        //     }
        // }
        // return res;
    }
}