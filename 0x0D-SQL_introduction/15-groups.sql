-- shows the number of records with the same score
-- in the table
SELECT score, COUNT(*) as number 
	FROM second_table
	GROUP BY score
	HAVING COUNT(*) > 0
	ORDER BY score DESC;
