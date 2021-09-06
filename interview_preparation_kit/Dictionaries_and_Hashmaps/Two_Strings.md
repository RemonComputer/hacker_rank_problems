# Two Strings

## Link:
https://www.hackerrank.com/challenges/two-strings/problem


## Explaination:
Check for at least one common character using a boolean array of characters. 


## Code:

```
string twoStrings(string s1, string s2) {
    bool common_chars['z' - 'a' + 1];
    for(bool& e:common_chars){
        e = false;
    }
    for(char& c:s1){
        common_chars[c - 'a' + 1] = true;
    }
    for(char& c:s2){
        if(common_chars[c - 'a' + 1]){
            return "YES";
        }
    }
    return "NO";
}


```
