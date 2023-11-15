-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT name
FROM first_table
GROUP BY score AS number
WHERE ORDER BY score DESC;
