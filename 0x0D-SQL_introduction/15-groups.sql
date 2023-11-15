-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT score FROM second_table
COUNT(score) AS number
GROUP BY score ORDER BY score DESC;
