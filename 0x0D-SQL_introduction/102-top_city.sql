-- except top 3
SELECT `city`, AVG(`value`) as `avg_temp`
from `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;