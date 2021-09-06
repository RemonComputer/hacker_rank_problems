# Making Anagrams

## Link:
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem


## Explaination:
Solved using the sum of absolute difference in letter count between the two strings.


## Code:

```
int* make_histogram(string a){
    int n = 'z' - 'a' + 1;
    int* hist = new int[n];
    for(int i = 0; i < n; i++){
        hist[i] = 0;
    }
    for(char& ch:a){
        hist[ch - 'a']++;
    }
    return hist;
}

int makeAnagram(string a, string b) {
    int* hista = make_histogram(a);
    int* histb = make_histogram(b);
    int ch_delete_cnt = 0;
    int n = 'z' - 'a' + 1;
    for(int i = 0; i < n; i++){
        ch_delete_cnt+= abs(hista[i] - histb[i]);
    }
    delete [] hista;
    delete [] histb;
    return ch_delete_cnt;
}


```
