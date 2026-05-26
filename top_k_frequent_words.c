#include <stdlib.h>
#include <string.h>

typedef struct {
    char* word;
    int freq;
} Node;

int compare(const void* a, const void* b) {

    Node* x = (Node*)a;
    Node* y = (Node*)b;

    // Higher frequency first
    if (x->freq != y->freq)
        return y->freq - x->freq;

    // Lexicographical order
    return strcmp(x->word, y->word);
}

char** topKFrequent(char** words, int wordsSize, int k, int* returnSize) {

    Node arr[wordsSize];
    int size = 0;

    // Count frequencies
    for (int i = 0; i < wordsSize; i++) {

        int found = 0;

        for (int j = 0; j < size; j++) {

            if (strcmp(arr[j].word, words[i]) == 0) {
                arr[j].freq++;
                found = 1;
                break;
            }
        }

        if (!found) {
            arr[size].word = words[i];
            arr[size].freq = 1;
            size++;
        }
    }

    // Sort
    qsort(arr, size, sizeof(Node), compare);

    // Prepare answer
    char** result = (char**)malloc(k * sizeof(char*));

    for (int i = 0; i < k; i++) {
        result[i] = arr[i].word;
    }

    *returnSize = k;

    return result;
}
