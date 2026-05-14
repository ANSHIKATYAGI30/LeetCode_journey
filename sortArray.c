#include <stdlib.h>

void countingSort(int* arr, int size, int exp) {

    int* output = (int*)malloc(size * sizeof(int));

    int count[10] = {0};

    // Count digits
    for(int i = 0; i < size; i++) {

        int digit = (arr[i] / exp) % 10;

        count[digit]++;
    }

    // Prefix sum
    for(int i = 1; i < 10; i++) {

        count[i] += count[i - 1];
    }

    // Build output array
    for(int i = size - 1; i >= 0; i--) {

        int digit = (arr[i] / exp) % 10;

        output[count[digit] - 1] = arr[i];

        count[digit]--;
    }

    // Copy back
    for(int i = 0; i < size; i++) {

        arr[i] = output[i];
    }

    free(output);
}

void radixSort(int* arr, int size) {

    if(size == 0) return;

    int maxVal = arr[0];

    for(int i = 1; i < size; i++) {

        if(arr[i] > maxVal) {

            maxVal = arr[i];
        }
    }

    for(int exp = 1; maxVal / exp > 0; exp *= 10) {

        countingSort(arr, size, exp);
    }
}

/**
 * Note: The returned array must be malloced.
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {

    int* positive =
        (int*)malloc(numsSize * sizeof(int));

    int* negative =
        (int*)malloc(numsSize * sizeof(int));

    int p = 0;
    int n = 0;

    // Separate positive and negative
    for(int i = 0; i < numsSize; i++) {

        if(nums[i] >= 0) {

            positive[p++] = nums[i];
        }
        else {

            negative[n++] = -nums[i];
        }
    }

    // Sort both
    radixSort(positive, p);

    radixSort(negative, n);

    int idx = 0;

    // Negatives in reverse order
    for(int i = n - 1; i >= 0; i--) {

        nums[idx++] = -negative[i];
    }

    // Positives
    for(int i = 0; i < p; i++) {

        nums[idx++] = positive[i];
    }

    free(positive);
    free(negative);

    *returnSize = numsSize;

    return nums;
}
