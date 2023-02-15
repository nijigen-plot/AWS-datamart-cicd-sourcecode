import re

import boto3


def lambda_handler(event, context):
    query = ''
    
    if 'query' in event:
        query = event['query']
    else:
        s3_bucket = event['bucket']
        object_key = event['file_key']
        
        s3 = boto3.client('s3')
        response_s3 = s3.get_object(Bucket = s3_bucket, Key = object_key)
        query = response_s3['Body'].read().decode('utf-8')
        
    table_detection = re.search(r"CREATE\s+TABLE\s+datamart\.([a-zA-Z0-9_-]+)\s+WITH", query)
    locate_detection = re.search(r"external_location\s*=\s*'(.*?)'", query)

    try:
        ctas_query = table_detection.group()
        target_table = 'DROP TABLE IF EXISTS ' + ctas_query.split()[2]
    # resultの中身がNonetypeの場合空のtarget_tableを返す
    except AttributeError:
        print('CTASクエリではなかったので事前テーブル削除をスルーします。')
        target_table = ''
        # スルーの分岐はStepFunctionsで書く
    
    try:
        location = locate_detection.group()
        s3uri = location.split()[2].replace("'","")
        s3uri_split = s3uri.split("/")
        target_bucket = s3uri_split[2]
        target_key = '/'.join(s3uri_split[3:])
    except AttributeError:
        target_bucket = ''
        target_key = ''

    # queryの中身が''の場合エラーをスロー
    if not query:
        raise Exception('クエリ文字列が正しく設定されませんでした')
        
    return {
        'table' : target_table,
        's3_bucket' : target_bucket,
        's3_key' : target_key,
        'query' : query
    }