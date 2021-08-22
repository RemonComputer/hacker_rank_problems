# Maps-STL

## Link:
https://www.hackerrank.com/challenges/cpp-maps/problem?


## Explaination:
Practise Using Map class


## Code:

```

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N, Y, q_type, new_Y;
    string X;
    bool st_found;
    map<string, int> m;
    map<string, int>::iterator found_itr;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> q_type >> X;
        found_itr = m.find(X);
        st_found = (found_itr != m.end());
        switch (q_type) {
            case 1:
                cin >> Y;
                if(st_found){
                    new_Y = found_itr->second + Y;
                    m.erase(found_itr);
                    m.insert(make_pair(X, new_Y));
                    //cout << "Found " << X << "With " << found_itr->second
                }else {
                    m.insert(make_pair(X, Y));
                }
                break;
            case 2:
                if(st_found){
                    m.erase(found_itr);
                }
                break;
            case 3:
                if(st_found){
                    cout << found_itr->second << endl;
                }else {
                    cout << 0 << endl;
                }
                break;
        };
    }
    return 0;
}





```
