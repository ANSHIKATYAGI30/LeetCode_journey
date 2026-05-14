#include <stdlib.h>
#include <string.h>

void countingSort(char** nums, int numsSize, int pos, int* indices) {

    int count[10] = {0};

    int* output = (int*)malloc(numsSize * sizeof(int));

    // Count digits
    for(int i = 0; i < numsSize; i++) {

        int digit = nums[indices[i]][pos] - '0';

        count[digit]++;
    }

    // Prefix sum
    for(int i = 1; i < 10; i++) {

        count[i] += count[i - 1];
    }

    // Stable sort (right to left)
    for(int i = numsSize - 1; i >= 0; i--) {

        int digit = nums[indices[i]][pos] - '0';

        output[count[digit] - 1] = indices[i];

        count[digit]--;
    }

    // Copy back
    for(int i = 0; i < numsSize; i++) {

        indices[i] = output[i];
    }

    free(output);
}

/**
 * Note: The returned array must be malloced.
 */
int* smallestTrimmedNumbers(
    char** nums,
    int numsSize,
    int** queries,
    int queriesSize,
    int* queriesColSize,
    int* returnSize
) {

    int len = strlen(nums[0]);

    int* ans = (int*)malloc(queriesSize * sizeof(int));

    // sorted[trim][i]
    int** sorted =
        (int**)malloc((len + 1) * sizeof(int*));

    int* indices =
        (int*)malloc(numsSize * sizeof(int));

    // Initial indices
    for(int i = 0; i < numsSize; i++) {

        indices[i] = i;
    }

    // Radix sort from rightmost digit
    for(int trim = 1; trim <= len; trim++) {

        int pos = len - trim;

        countingSort(nums, numsSize, pos, indices);

        sorted[trim] =
            (int*)malloc(numsSize * sizeof(int));

        memcpy(sorted[trim],
               indices,
               numsSize * sizeof(int));
    }

    // Answer queries
    for(int i = 0; i < queriesSize; i++) {

        int k = queries[i][0];

        int trim = queries[i][1];

        ans[i] = sorted[trim][k - 1];
    }

    *returnSize = queriesSize;

    return ans;
}
