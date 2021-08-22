# Lower Bound-STL

## Link:
https://www.hackerrank.com/challenges/cpp-lower-bound/problem


## Explaination:
Use Lower_bound function to solve the problem, don't forget to add 1 to the lower_iter iterator 


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
    int N, tmp;
    cin >> N;
    vector<int> arr(N); // Reading number of items in array 
    for(auto& p: arr){ // initializing each element
        cin >> p;
    }
    vector<int>::iterator lower_itr;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> tmp;
        lower_itr = lower_bound(arr.begin(), arr.end(), tmp);
        if(*lower_itr == tmp){
            cout << "Yes ";
        }else {
            cout << "No ";
        }
        cout << (lower_itr - arr.begin() + 1) << endl;
    }
    return 0;
}


```
