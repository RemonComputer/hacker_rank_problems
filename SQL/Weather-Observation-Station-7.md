# Weather Observation Station

## Link:
https://www.hackerrank.com/challenges/weather-observation-station-7/problem


## Explaination:
Using REGEXP_LIKE function with **$** as endline operator, also with DISTINCT function.


## Code:

```
/*
Enter your query here.
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE REGEXP_LIKE(CITY, '[aeoiu]$')


```
