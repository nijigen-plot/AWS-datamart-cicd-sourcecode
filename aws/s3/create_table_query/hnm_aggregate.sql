CREATE TABLE datamart.hnm_aggregate WITH (
    format = 'PARQUET',
    external_location = 's3://quark-datamart/hnm_aggregate/'
) AS
SELECT club_member_status,
    AVG(try_cast(recency as double)) as avg_recency,
    AVG(try_cast(total_purchase as double)) as avg_total_purchase
FROM h_and_m.customers
GROUP BY club_member_status