/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function(root) {
    
    if (!root) return 0;

    let leftHeight = 0;
    let rightHeight = 0;

    let left = root;
    let right = root;

    // Find left height
    while (left) {
        leftHeight++;
        left = left.left;
    }

    // Find right height
    while (right) {
        rightHeight++;
        right = right.right;
    }

    // Perfect binary tree
    if (leftHeight === rightHeight) {
        return Math.pow(2, leftHeight) - 1;
    }

    // Otherwise count recursively
    return 1 + countNodes(root.left) + countNodes(root.right);
};
