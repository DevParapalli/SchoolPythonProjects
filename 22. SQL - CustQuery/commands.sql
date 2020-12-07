/*  */
SELECT cust_country,
    count(*)
FROM cust_table
GROUP BY cust_country;