--  a script that computes the score average of all records in the table second_table of the database hbtn_0c_0
INSERT INTO second_table average
VALUES (SELECT AVG(score) FROM second_table);
