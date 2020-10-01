# Variable Sized Arrays
 

## Link: https://www.hackerrank.com/challenges/variable-sized-arrays/problem



## Explaination:

Allocate 2d Array with dynamic allocation


## Code:

```

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q;
    cin >> n >> q;
    int* arr[n];
    int n_i_size;
    for(int i=0; i < n; i++){
        cin >> n_i_size;
        arr[i] = new int[n_i_size];
        for(int j=0; j < n_i_size; j++){
            cin >> arr[i][j];
        }
    }
    int idx_i, idx_j;
    for(int i=0; i < q; i++){
        cin >> idx_i >> idx_j;
        cout << arr[idx_i][idx_j] << endl;
    }
    return 0;
}

```
