CREATE TABLE datamart.riiid_aggregate WITH (
    format = 'PARQUET',
    external_location = 's3://quark-datamart/riiid_aggregate/'
) AS
SELECT user_id,
    COUNT(answered_correctly) as answer_number,
    AVG(answered_correctly) as correct_answer_rate
FROM main_data.riiid_train_data
GROUP BY user_id