#include <stdlib.h>

char* convertToTitle(int columnNumber) {
    
    char* result = (char*)malloc(10 * sizeof(char));
    int index = 0;

    while (columnNumber > 0) {

        columnNumber--; // shift to 0-based

        result[index++] = (columnNumber % 26) + 'A';

        columnNumber /= 26;
    }

    result[index] = '\0';

    // reverse string
    for (int i = 0, j = index - 1; i < j; i++, j--) {
        char temp = result[i];
        result[i] = result[j];
        result[j] = temp;
    }

    return result;
}
