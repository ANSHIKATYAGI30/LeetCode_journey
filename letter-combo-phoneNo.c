#include <stdlib.h>
#include <string.h>

char* mapping[] = {
    "",     // 0
    "",     // 1
    "abc",  // 2
    "def",  // 3
    "ghi",  // 4
    "jkl",  // 5
    "mno",  // 6
    "pqrs", // 7
    "tuv",  // 8
    "wxyz"  // 9
};
void backtrack(char* digits, int index,
               char* current,
               char** result,
               int* returnSize) {
    // complete combination formed
    if(digits[index] == '\0') {
        result[*returnSize] = strdup(current);
        (*returnSize)++;
        return;
    }
    char* letters = mapping[digits[index] - '0'];
    for(int i = 0; letters[i] != '\0'; i++) {
        current[index] = letters[i];
        backtrack(digits, index + 1,
                  current, result, returnSize);
    }
}
char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    if(strlen(digits) == 0) {
        return NULL;
    }
    // Maximum possible combinations = 4^n
    char** result = (char**)malloc(10000 * sizeof(char*));
    char current[10];
    backtrack(digits, 0, current, result, returnSize);

    return result;
}
