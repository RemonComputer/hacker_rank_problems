# VEctor Sort 

## Link:

https://www.hackerrank.com/challenges/vector-sort/problem

## Explaination:

Read a vector of numbers from STDIN and sort it and print it 

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
    int n, n_i;
    cin >> n;
    vector<int> v;
    for(int i=0; i<n; i++){
        cin >> n_i;
        v.push_back(n_i);
    }
    sort(v.begin(), v.end());
    int size = v.size();
    for(auto v_i=v.begin(); v_i != v.end(); ++v_i){
        cout << *v_i << " ";
    }
    return 0;
}


```
