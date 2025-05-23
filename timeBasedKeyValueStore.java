class TimeMap {
    HashMap<String, TreeMap<Integer, String>> timeMap = new HashMap<>();
    public TimeMap() {
        this.timeMap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        TreeMap<Integer, String> entry = timeMap.getOrDefault(key, new TreeMap<Integer, String>());
        entry.put(timestamp, value);
        timeMap.put(key, entry);
    }
    
    public String get(String key, int timestamp) {
        TreeMap<Integer, String> entry = timeMap.getOrDefault(key, new TreeMap<Integer, String>());
        if(entry.isEmpty()) return "";
        Map.Entry<Integer, String> element = entry.floorEntry(timestamp);
        if(element == null) return "";
        return element.getValue();
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
