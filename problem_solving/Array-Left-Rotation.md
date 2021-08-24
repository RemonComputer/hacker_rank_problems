# Array Left Rotation

## Link:
https://www.hackerrank.com/challenges/array-left-rotation/problem


## Explaination:
Left Rotation by d is equivilant to right rotation by size(array) - d, and you can get the final element position by ((i + right_rotation) % size(array))


## Code:

```
vector<int> rotateLeft(int d, vector<int> arr) {
    int n = arr.size();
    vector<int> rotatedArr(n);
    int right_d = n - d;
    for(int i = 0; i < n; i++){
        // cout << i << endl;
        cout << ((i + right_d) % n) << endl;
        rotatedArr[(i + right_d) % n] = arr[i];
    }
    return rotatedArr;
}


```
