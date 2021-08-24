# Reverse-Array

## Link:
https://www.hackerrank.com/challenges/arrays-ds/problem


## Explaination:
Looping until middle index and reversing each pair


## Code:

```
vector<int> reverseArray(vector<int> a) {
    int middle_idx = a.size() / 2;
    int max_idx = a.size() - 1;
    int tmp;
    for(int i = 0; i < middle_idx; i++){
        tmp = a.at(max_idx - i);
        a.at(max_idx - i) = a.at(i);
        a.at(i) = tmp;
    }
    return a;
}
```
