#include <stdlib.h>

typedef struct {
    int num;
    int freq;
} Node;

int compare(const void* a, const void* b) {

    Node* x = (Node*)a;
    Node* y = (Node*)b;

    return y->freq - x->freq;
}

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {

    Node arr[numsSize];
    int size = 0;

    // Count frequencies
    for (int i = 0; i < numsSize; i++) {

        int found = 0;

        for (int j = 0; j < size; j++) {

            if (arr[j].num == nums[i]) {

                arr[j].freq++;
                found = 1;
                break;
            }
        }

        if (!found) {

            arr[size].num = nums[i];
            arr[size].freq = 1;
            size++;
        }
    }

    // Sort by frequency descending
    qsort(arr, size, sizeof(Node), compare);

    // Store top k elements
    int* result = (int*)malloc(k * sizeof(int));

    for (int i = 0; i < k; i++) {

        result[i] = arr[i].num;
    }

    *returnSize = k;

    return result;
}
