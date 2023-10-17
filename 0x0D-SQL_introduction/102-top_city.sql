-- except top 3
SELECT `city`, AVG(`value`) as `avg_temp`
from `temperatures`
GROUP BY `city`
WHERE `month` == 7 or `month` == 8
ORDER BY `avg_temp` DESC
LIMIT 3;