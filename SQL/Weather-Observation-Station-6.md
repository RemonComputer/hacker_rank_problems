# Weather-Observation-Station-6

## Link:
https://www.hackerrank.com/challenges/weather-observation-station-6/problem


## Explaination:
Using REGEXP_LIKE function to achieve regular expression like matching


## Code:

```
/*
Enter your query here.
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE REGEXP_LIKE(CITY, '^[aeiou]');


```
