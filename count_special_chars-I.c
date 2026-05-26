int numberOfSpecialChars(char* word) {

    int lower[26] = {0};
    int upper[26] = {0};

    int i = 0;

    while(word[i]) {

        if(word[i] >= 'a' && word[i] <= 'z') {
            lower[word[i] - 'a'] = 1;
        }
        else if(word[i] >= 'A' && word[i] <= 'Z') {
            upper[word[i] - 'A'] = 1;
        }

        i++;
    }

    int count = 0;

    for(i = 0; i < 26; i++) {

        if(lower[i] && upper[i]) {
            count++;
        }
    }

    return count;
}
