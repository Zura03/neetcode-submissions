class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparing(a -> a[0]));

        for (int[] p : points){
            int d = (int) (Math.pow(p[0], 2) + Math.pow(p[1], 2));
            minHeap.offer(new int[] {d, p[0], p[1]});
        }

        int[][] res = new int[k][2];
        for (int i = 0; i < k; i++){
            int[] point = minHeap.poll();
            res[i] = new int[] {point[1], point[2]};
        }
        return res;

    }
}
