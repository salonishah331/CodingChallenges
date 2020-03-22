// Find the height of a tree


private int height(root) {
    int height = 0;
    if (root == null) {
        return height;
    }
    else {
        int left = height(root.left);
        int right = height(root.right);
        
        if (left > right) {
            return left + 1;
        }
        else {
            return right + 1;
        }
    }
}