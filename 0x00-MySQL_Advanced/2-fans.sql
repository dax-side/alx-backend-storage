-- script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
-- Import table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans

-- select columns
SELECT origin,
	SUM(fans) as nb_fans
       	FROM metal_bands
	GROUP BY 1
	ORDER BY 2 DESC;
