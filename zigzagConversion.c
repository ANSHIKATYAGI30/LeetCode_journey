#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {

    if(numRows == 1) {
        return s;
    }

    int len = strlen(s);

    // Create rows
    char** rows = (char**)malloc(numRows * sizeof(char*));

    for(int i = 0; i < numRows; i++) {

        rows[i] = (char*)calloc(len + 1, sizeof(char));
    }

    int currentRow = 0;
    int direction = 1;

    // Fill rows
    for(int i = 0; i < len; i++) {

        int rowLen = strlen(rows[currentRow]);

        rows[currentRow][rowLen] = s[i];

        // Change direction
        if(currentRow == 0) {
            direction = 1;
        }
        else if(currentRow == numRows - 1) {
            direction = -1;
        }

        currentRow += direction;
    }

    // Final answer
    char* ans = (char*)malloc((len + 1) * sizeof(char));

    ans[0] = '\0';

    for(int i = 0; i < numRows; i++) {

        strcat(ans, rows[i]);

        free(rows[i]);
    }

    free(rows);

    return ans;
}
