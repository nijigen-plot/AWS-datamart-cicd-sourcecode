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
    
    # queryの中身が''の場合エラーをスロー
    if not query:
        raise Exception('クエリ文字列が正しく設定されませんでした')
    
    return {
        'query' : query
    }
