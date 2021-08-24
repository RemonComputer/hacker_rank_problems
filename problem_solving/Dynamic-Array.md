# Dynamic Array
 
## Link:
https://www.hackerrank.com/challenges/dynamic-array/problem


## Explaination:
Just use vector for ssynamic arrays and the rest is striaght forward


## Code:

```
vector<int> dynamicArray(int n, vector<vector<int>> queries) {
    int lastAnswer = 0;
    vector<int> arr[n];
    vector<int> result;
    int idx, x, y;
    for(auto& q:queries){
        x = q[1];
        y = q[2];
        idx = (x ^ lastAnswer) % n;
        switch (q[0]) {
            case 1:
                arr[idx].push_back(y);
                break;
            case 2:
                lastAnswer = arr[idx][y % arr[idx].size()];
                result.push_back(lastAnswer);
                break;
        }
    }
    return result;
}


```
