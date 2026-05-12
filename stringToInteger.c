#include <limits.h>

int myAtoi(char* s) {

    int i = 0;

    // Skip whitespaces
    while(s[i] == ' ') {
        i++;
    }

    // Check sign
    int sign = 1;

    if(s[i] == '-') {
        sign = -1;
        i++;
    }
    else if(s[i] == '+') {
        i++;
    }

    int result = 0;

    // Read digits
    while(s[i] >= '0' && s[i] <= '9') {

        int digit = s[i] - '0';

        // Overflow check
        if(result > (INT_MAX - digit) / 10) {

            return sign == 1 ? INT_MAX : INT_MIN;
        }

        result = result * 10 + digit;

        i++;
    }

    return result * sign;
}
