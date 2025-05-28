// follow the pattern from this solution
//https://leetcode.com/problems/web-crawler-multithreaded/solutions/1590423/java-solution-futures-concurrenthashmap-parallel-stream/
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
class Solution {
    private String hostname;
    private final Set<String> visited = ConcurrentHashMap.newKeySet();
    private final ExecutorService executor = Executors.newFixedThreadPool(8);
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        this.hostname = startUrl.substring(7).split("/")[0]; // strip the "http://"

        //start recursive crawl
        CompletableFuture<Void> crawlFuture = crawlUrl(startUrl, htmlParser);

        //wait for all tasks to finish
        crawlFuture.join();

        //shutdown thread pool
        executor.shutdown();
        
        return new ArrayList<String>(visited);
    }

    private CompletableFuture<Void> crawlUrl(String url, HtmlParser parser) {
        if(!belongToHostname(url) || !visited.add(url))
            return CompletableFuture.completedFuture(null);
        
        return CompletableFuture.supplyAsync( () -> parser.getUrls(url), executor )
            .thenCompose(urls ->{
                List<CompletableFuture<Void>> futures = urls.stream()
                    .map(link -> crawlUrl(link, parser))
                    .collect(Collectors.toList());
                return CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]) );
            });
    }

    private boolean belongToHostname(String url){
        String urlHost = url.substring(7).split("/")[0];
        return urlHost.equals(this.hostname);
    }
}
/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
// class Solution {
//     String hostname;
//     public List<String> crawl(String startUrl, HtmlParser htmlParser) {
//         this.hostname = startUrl.substring(7).split("/")[0]; // strip the "http://"
//         ArrayDeque<String> queue = new ArrayDeque<String>();
//         Set<String> visited = new HashSet<String>();

//         queue.addLast(startUrl);
//         while(!queue.isEmpty()){
//             // int loopSize = queue.size();
//             for(int i = 0; i < queue.size(); i++){
//                 String currUrl = queue.removeFirst();
//                 visited.add(currUrl);

//                 for(String url: htmlParser.getUrls(currUrl)){
//                     if(!visited.contains(url) && belongToHostname(url)) queue.addLast(url);
//                 }
//             }
//         }
//         return new ArrayList<String>(visited);
//     }
//     private Boolean belongToHostname(String url) {
//         String urlHost = url.substring(7).split("/")[0];
//         return urlHost.equals(this.hostname);
//     }
// }
