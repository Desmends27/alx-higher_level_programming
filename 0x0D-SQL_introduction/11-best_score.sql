-- lists all the records (name and score) with a score >= 10
-- int the second table
SELECT score, name FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
