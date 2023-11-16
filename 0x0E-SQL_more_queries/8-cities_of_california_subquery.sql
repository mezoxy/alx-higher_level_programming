-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities
WHERE states.name = 'California' AND states.id = state_id
ORDER BY cities.id ASC;
