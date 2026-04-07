import java.util.*;
import java.io.*;

class Two {
    public static void main(String[] args) throws Exception {
        TreeMap<String, Integer> map = new TreeMap<>();
        BufferedReader br = new BufferedReader(new FileReader("input.txt")); // create this file
        String line;
        while ((line = br.readLine()) != null) {
            String[] words = line.toLowerCase().split("\\s+");
            for (String w : words) {
                if (!w.isEmpty()) map.put(w, map.getOrDefault(w, 0) + 1);
            }
        }
        br.close();

        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
            public int compare(Map.Entry<String, Integer> a, Map.Entry<String, Integer> b) {
                return b.getValue().compareTo(a.getValue()); // descending frequency
            }
        });

        System.out.println("Greatest (most frequent): " + list.get(0));
        System.out.println("Least (least frequent): " + list.get(list.size() - 1));
    }
}