import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response_s3 = s3.list_objects_v2(
        Bucket = event['bucket'],
        Prefix = event['file_key']
        )
    
    try:    
        file_keys = list(map(lambda x : {"Key" : x['Key']}, response_s3['Contents']))
    
        s3.delete_objects(
            Bucket = 'quark-datamart',
            Delete = {
                'Objects' : file_keys
            }
        )
        print('指定のプレフィックス下のオブジェクトを削除しました。')
    except KeyError:
        print('指定のプレフィックス下にオブジェクトは存在していませんでした。')
