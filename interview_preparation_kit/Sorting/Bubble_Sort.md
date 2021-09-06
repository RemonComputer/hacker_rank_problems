# Bubble Sort

## Link:
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem


## Explaination:
Count swaps in bubble sort and sort the array.


## Code:

```
void countSwaps(vector<int> a) {
    int n_swaps = 0, tmp;
    for(int i = 0; i < a.size() - 1; i++){
        for(int j = i + 1; j < a.size(); j++){
            if(a[j] < a[i]){
                tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
                n_swaps++;
            }
        }
    }
    cout << "Array is sorted in " << n_swaps << " swaps." << endl;
    cout << "First Element: " << a[0] << endl;
    cout << "Last Element: " << a[a.size() - 1] << endl;
}


```
