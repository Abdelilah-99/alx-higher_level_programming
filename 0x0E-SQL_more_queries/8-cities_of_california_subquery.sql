-- get all cities of callifornia that can be found in database
SELECT id, name from cities
WHERE id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;