-- lists all records of the table second_table
-- rows which have nul values are not included
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
