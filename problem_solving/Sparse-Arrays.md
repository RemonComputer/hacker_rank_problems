# Sparse Arrays

## Link:
https://www.hackerrank.com/challenges/sparse-arrays/problem


## Explaination:
Just use a counts map to count string occurances


## Code:

```
vector<int> matchingStrings(vector<string> strings, vector<string> queries) {
    unordered_map<string, int> count_map(queries.size());
    // Initialize the map
    for(auto& s:queries){
        count_map.insert(make_pair(s, 0));
    }
    // Count the occurances
    for(auto& s:strings){
        auto found_itr = count_map.find(s);
        if(found_itr != count_map.end()){
            found_itr->second++;
        }
    }
    // Collecting the counts
    vector<int> result;
    for(auto& s:queries){
        auto found_itr = count_map.find(s);
        if(found_itr != count_map.end()){
            result.push_back(found_itr->second);
        }
    }
    return result;
}

```
