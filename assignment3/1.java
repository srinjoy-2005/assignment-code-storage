import java.util.*;

class One {
    private static int printed = 0;
    private static final int MAX_EXAMPLES = 5;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n and k: ");
        int n = sc.nextInt();
        int k = sc.nextInt();
        int x = Math.min(k, n / 2);
        System.out.println("x = " + x);
        System.out.println("Some combinations of types (1 to " + k + "):");
        if (x == 0) {
            System.out.println("No sweets to eat.");
            return;
        }
        System.out.println("Example combinations:");
        generateCombinations(1, k, x, new ArrayList<>());
        if (printed >= MAX_EXAMPLES) System.out.println((binomial(k, x)) + " Total combinations");
    }

    private static void generateCombinations(int start, int k, int x, List<Integer> current) {
        if (printed >= MAX_EXAMPLES) return;
        if (current.size() == x) {
            System.out.println(current);
            printed++;
            return;
        }
        for (int i = start; i <= k; i++) {
            current.add(i);
            generateCombinations(i + 1, k, x, current);
            current.remove(current.size() - 1);
            if (printed >= MAX_EXAMPLES) return;
        }
    }

    private static long binomial(int n, int k) { // just for info
        if (k > n - k) k = n - k;
        long res = 1;
        for (int i = 1; i <= k; i++) res = res * (n - k + i) / i;
        return res;
    }
}