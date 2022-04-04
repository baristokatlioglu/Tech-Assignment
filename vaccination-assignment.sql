
-- Assigning 0 to the variable daily vaccinations for countries without vaccination records
WITH no_vac AS (
	SELECT 
		country
	FROM dbo.country_vaccination_stats
	GROUP BY country
	HAVING COUNT(daily_vaccinations) = 0
)
UPDATE dbo.country_vaccination_stats
SET daily_vaccinations = 0
WHERE country = (SELECT country FROM no_vac);



-- Assingning Median to NULL values
WITH mdn AS (
	SELECT 
		DISTINCT country, PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY daily_vaccinations) OVER (PARTITION BY country) AS median
	FROM country_vaccination_stats
)
UPDATE dbo.country_vaccination_stats
SET daily_vaccinations = (SELECT median FROM mdn WHERE country = dbo.country_vaccination_stats.country)
WHERE daily_vaccinations IS NULL ;



