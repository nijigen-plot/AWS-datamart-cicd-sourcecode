CREATE TABLE datamart.practice_sales WITH (
    format = 'PARQUET',
    external_location = 's3://quark-datamart/practice_sales/'
) AS
SELECT *
FROM main_data.practice_sales