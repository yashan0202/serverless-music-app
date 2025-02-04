import json
import boto3
import uuid

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MusicMetadata')

def lambda_handler(event, context):
    file_content = event['body']
    file_name = str(uuid.uuid4()) + ".mp3"
    bucket_name = "serverless-music-app"

    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

    # Save metadata in DynamoDB
    table.put_item(Item={
        'song_id': file_name,
        'title': event['title'],
        'artist': event['artist'],
        'duration': event['duration'],
        'file_url': f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'File uploaded successfully'})
    }
