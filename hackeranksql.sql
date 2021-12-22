/* write  a query to print ids of the companies  that have more than 10000 employees, in ascending order */


SELECT ID FROM  COMPANY  WHERE employees > 10000 ORDER BY id ASC;

/*write a Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

The CITY table is described as follows*/

Select Name from CITY where CountryCode = 'USA' and Population > 120000;

/* write a query for all columns(attribute)for every row in the city table*/

Select * from CITY;

/* Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.*/

Select CITY  from  STATION WHERE ID % 2 = 0;

/*Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows */

Select count(distinct CITY) - count(*) from STATION;


/* write a Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
from The STATION table */

/*Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.*/
/* query two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.*/
/* query two city */


select city, length(city) from station
order by length(city),city asc
limit 1;
select city, length(city) from station
order by length(city) desc
limit 1;