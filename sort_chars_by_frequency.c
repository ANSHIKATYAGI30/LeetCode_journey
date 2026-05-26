#include <stdlib.h>
#include <string.h>

typedef struct {
    char ch;
    int freq;
} Node;

int compare(const void* a, const void* b) {

    Node* x = (Node*)a;
    Node* y = (Node*)b;

    return y->freq - x->freq;
}

char* frequencySort(char* s) {

    int freq[128] = {0};

    // Count frequency
    for (int i = 0; s[i]; i++) {
        freq[s[i]]++;
    }

    Node arr[128];
    int size = 0;

    // Store characters with frequency
    for (int i = 0; i < 128; i++) {

        if (freq[i] > 0) {

            arr[size].ch = i;
            arr[size].freq = freq[i];
            size++;
        }
    }

    // Sort by frequency descending
    qsort(arr, size, sizeof(Node), compare);

    int n = strlen(s);

    char* result = (char*)malloc((n + 1) * sizeof(char));

    int idx = 0;

    // Build answer
    for (int i = 0; i < size; i++) {

        for (int j = 0; j < arr[i].freq; j++) {

            result[idx++] = arr[i].ch;
        }
    }

    result[idx] = '\0';

    return result;
}
