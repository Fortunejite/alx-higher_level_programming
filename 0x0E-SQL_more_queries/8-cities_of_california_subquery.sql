-- My SQL qurrey
SELECT *
FROM cities 
WHERE state_id =
(SELECT id FROM states WHERE name = 'California')
ORDER BY state_id ASC;