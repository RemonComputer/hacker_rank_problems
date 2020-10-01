# Vector Erase  

## Link:

https://www.hackerrank.com/challenges/vector-erase/problem

## Explaination:

Erase Indices from A Vector

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
    int n, n_i, q_1, q_2_1, q_2_2;
    cin >> n;
    vector<int> v;
    // cout << "Log 1" << endl;
    for(int i=0; i < n; i++){
        cin >> n_i;
        v.push_back(n_i);
    }
    // cout << v.size() << endl;
    // cout << "Log 2" << endl;
    cin >> q_1 >> q_2_1 >> q_2_2;
    // cout << "Log 3" << endl;
    v.erase(v.begin() + (q_1 - 1));
    // cout << "Log 3_2" << endl;
    v.erase(v.begin() + (q_2_1 - 1), v.begin() + (q_2_2 - 1));
    // cout << "Log 4" << endl;
    cout << v.size() << endl;
    // cout << "Log 5" << endl;
    for(auto v_i = v.begin(); v_i != v.end(); ++v_i){
        cout << *v_i << " ";
    }
    return 0;
}


```
