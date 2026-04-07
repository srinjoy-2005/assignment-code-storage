import java.util.*;

class Three{
    static class TreeNode {
        String val;
        TreeNode left, right;
        TreeNode(String v) { val = v; }
    }

    public static void main(String[] args) {
        String[] preorder = {"Grandpa", "Dad", "Son", "Daughter", "Mom", "Uncle", "Cousin1", "Cousin2"};
        String[] inorder = {"Son", "Dad", "Daughter", "Grandpa", "Cousin1", "Uncle", "Cousin2", "Mom"};
        
        TreeNode root = buildTree(preorder, inorder);
        printCousins(root);
    }

    private static TreeNode buildTree(String[] pre, String[] in) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < in.length; i++) map.put(in[i], i);
        return build(pre, 0, pre.length - 1, in, 0, in.length - 1, map);
    }

    private static TreeNode build(String[] pre, int pStart, int pEnd,
                                  String[] in, int iStart, int iEnd, Map<String, Integer> map) {
        if (pStart > pEnd) return null;
        TreeNode root = new TreeNode(pre[pStart]);
        int rootIdx = map.get(pre[pStart]);
        int leftLen = rootIdx - iStart;
        root.left = build(pre, pStart + 1, pStart + leftLen, in, iStart, rootIdx - 1, map);
        root.right = build(pre, pStart + leftLen + 1, pEnd, in, rootIdx + 1, iEnd, map);
        return root;
    }

    private static void printCousins(TreeNode root) {
        if (root == null) return;
        Map<Integer, List<String>> depthMap = new HashMap<>();
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> dq = new LinkedList<>();
        q.add(root); dq.add(0);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            int d = dq.poll();
            depthMap.computeIfAbsent(d, k -> new ArrayList<>()).add(node.val);
            if (node.left != null) { q.add(node.left); dq.add(d + 1); }
            if (node.right != null) { q.add(node.right); dq.add(d + 1); }
        }
        System.out.println("Cousins in family generations:");
        for (Map.Entry<Integer, List<String>> e : depthMap.entrySet()) {
            if (e.getValue().size() >= 2) {
                System.out.println("  Generation " + e.getKey() + ": " + e.getValue());
            }
        }
    }
}