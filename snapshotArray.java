//editorial solution, use treemap so that binary search is used when locating the right snap version.
class SnapshotArray {
    private int snapId = 0;
    TreeMap<Integer, Integer>[] records;
    public SnapshotArray(int length) {
        records = new TreeMap[length];
        for(int i = 0; i< length; i++){
            records[i] = new TreeMap<Integer, Integer>();
            records[i].put(snapId, 0);
        }
    }
    
    public void set(int index, int val) {
        TreeMap<Integer, Integer> record = records[index];
        record.put(snapId, val);
    }
    
    public int snap() {
        return snapId++;
    }
    
    public int get(int index, int snap_id) {
        TreeMap<Integer, Integer> record = records[index];
        return record.floorEntry(snap_id).getValue();
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */


 // designated Versioned Num class, time limit exceed
 class VersionedNum {
    int curr;
    // list of pair of (version, value)
    List<int[]> versioned;
    public VersionedNum(int number){
        this.curr = number;
        this.versioned = new ArrayList<>();
    }
    public void setNumber(int number){
        this.curr = number;
    }
    public void snapshot(int version){
        int size = this.versioned.size();
        if(this.versioned.isEmpty() || curr != this.versioned.get(size -1)[1]){
            this.versioned.add(new int[]{version, curr});
        }
        // System.out.println(String.join(", ",
        //     this.versioned.stream().map(it -> it[0]+" "+it[1]).collect(Collectors.toList())
        // ));
    }
    public int getVersioned(int version){

        List<int[]> optPicked = this.versioned.stream().filter(it -> it[0] <= version ).collect(Collectors.toList());

        // System.out.println("optPicked " + version +" list is "+ String.join(", ",
        //     optPicked.stream().map(it -> it[0]+" "+it[1]).collect(Collectors.toList())
        // ));

        int[] picked = optPicked.get(optPicked.size() -1);

        return picked[1];
    }
}
class SnapshotArray {
    private VersionedNum[] snap;
    private int SNAPSHOT_VERSION;
    public SnapshotArray(int length) {
        this.SNAPSHOT_VERSION = 0;
        this.snap = new VersionedNum[length];
        for (int i = 0; i < this.snap.length; i++) {
            this.snap[i] = new VersionedNum(0);
        }
    }
    
    public void set(int index, int val) {
        VersionedNum vn = this.snap[index];
        vn.setNumber(val);
    }
    
    public int snap() {
        for (int i = 0; i < this.snap.length; i++) {
            VersionedNum vn = this.snap[i];
            vn.snapshot(this.SNAPSHOT_VERSION);
        }
        return this.SNAPSHOT_VERSION++;
    }
    
    public int get(int index, int snap_id) {
        VersionedNum vn = this.snap[index];
        return vn.getVersioned(snap_id);
    }
}



 // memory limit exceeded solution
class SnapshotArray {
    private ArrayList<int[]> snap;
    private int[] array;
    private int ARRAY_SIZE;

    public SnapshotArray(int length) {
        this.snap = new ArrayList<>();
        this.array = new int[length];
        this.ARRAY_SIZE = length;
    }
    
    public void set(int index, int val) {
        this.array[index] = val;
    }
    
    public int snap() {
        int[] cloneArr = this.array.clone();
        this.snap.add(cloneArr);
        return this.snap.size() -1;
    }
    
    public int get(int index, int snap_id) {
        int[] versioned = this.snap.get(snap_id);
        if(index < this.ARRAY_SIZE) return versioned[index];
        return 0;
    }
}
