SELECT count(*) as USERS
FROM user_info
WHERE year(joined) = 2021 
     AND age BETWEEN 20 AND 29