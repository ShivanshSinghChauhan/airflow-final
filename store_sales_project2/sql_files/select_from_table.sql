SELECT DATE, STORE_LOCATION, ROUND((SUM(SP) - SUM(CP)), 2) AS lc_profit FROM clean_store_transactions WHERE DATE = STR_TO_DATE("26/11/19", '%d/%m/%Y') GROUP BY STORE_LOCATION ORDER BY lc_profit DESC INTO OUTFILE '/store_files_mysql/location_wise_profit.csv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
SELECT DATE, STORE_ID, ROUND((SUM(SP) - SUM(CP)), 2) AS st_profit FROM clean_store_transactions WHERE DATE = STR_TO_DATE("26/11/19", '%d/%m/%Y') GROUP BY STORE_ID ORDER BY st_profit DESC INTO OUTFILE '/store_files_mysql/store_wise_profit.csv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';

















