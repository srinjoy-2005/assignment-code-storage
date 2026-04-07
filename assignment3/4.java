import java.util.*;

class Four {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of teams: ");
        int m = sc.nextInt();
        List<Integer> scores = new ArrayList<>();
        System.out.println("Enter the scores:");
        for (int i = 0; i < m; i++) {
            scores.add(sc.nextInt());
        }

        List<Integer> sortedScores = new ArrayList<>(scores);
        Collections.sort(sortedScores, Collections.reverseOrder());
        
        List<Integer> allowedScores = new ArrayList<>();
        long totalRunningProduct = 1;

        for (int score : sortedScores) {
            // Check if adding this score keeps the product within int range
            if (totalRunningProduct * score <= Integer.MAX_VALUE && totalRunningProduct * score > 0) {
                totalRunningProduct *= score;
                allowedScores.add(score);
            } else {
                System.out.println("Removing high scorer: " + score);
            }
        }

        List<Integer> filteredScores = new ArrayList<>();
        for (int originalScore : scores) {
            if (allowedScores.contains(originalScore)) {
                filteredScores.add(originalScore);
                allowedScores.remove(Integer.valueOf(originalScore));
            }
        }

        int n = filteredScores.size();
        if (n == 0) {
            System.out.println("No valid scores remaining.");
            return;
        }
        int[] result = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        // Prefix products
        left[0] = 1;
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1] * filteredScores.get(i - 1);
        }

        // Suffix products
        right[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            right[i] = right[i + 1] * filteredScores.get(i + 1);
        }

        System.out.println("\nFinal Products (except self) for valid scores:");
        for (int i = 0; i < n; i++) {
            result[i] = left[i] * right[i];
            System.out.print(result[i] + " ");
        }
        System.out.println();
    }
}