-- import a file and showing avrge temp of each unique city and then grp them and then sorting in desc order
SELECT `city`, AVG(`value`) as `avg_temp`
from `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;