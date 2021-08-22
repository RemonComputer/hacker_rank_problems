# Sets-STL

## Link:
https://www.hackerrank.com/challenges/cpp-sets/problem



## Explaination:
Practical usage of sets


## Code:

```
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, q_n, q_x;
    set<int> s;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> q_n >> q_x;
        switch (q_n) {
            case 1:
                s.insert(q_x);
                break;
            case 2:
                s.erase(q_x);
                break;
            case 3:
                auto el_itr = s.find(q_x);
                if (el_itr == s.end()) {
                    cout << "No" << endl;
                }else {
                    cout << "Yes" << endl;
                }
        }
    }
    return 0;
}






```
