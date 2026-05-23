/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverse(struct ListNode* head) {

    struct ListNode* prev = NULL;
    struct ListNode* curr = head;

    while (curr != NULL) {

        struct ListNode* next = curr->next;

        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}

bool isPalindrome(struct ListNode* head) {

    if (head == NULL || head->next == NULL)
        return true;

    // Find middle
    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse second half
    struct ListNode* second = reverse(slow);

    struct ListNode* first = head;

    // Compare both halves
    while (second) {

        if (first->val != second->val)
            return false;

        first = first->next;
        second = second->next;
    }

    return true;
}
