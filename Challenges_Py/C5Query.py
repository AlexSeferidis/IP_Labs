## Remove All Movies Released Before 2000 ##

from decimal import Decimal
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


def delete_movies_before(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')

    # Scan the table to get all movies released before the specified year
    response = table.scan(
        FilterExpression=Key('year').lt(year)
    )

    # Delete each item found in the scan
    for item in response['Items']:
        try:
            table.delete_item(
                Key={
                    'year': item['year'],
                    'title': item['title']
                }
            )
            print(f"Deleted: {item['title']} ({item['year']})")
        except ClientError as e:
            print(f"Failed to delete {item['title']} ({item['year']}): {e}")

    return response['Items']


if __name__ == '__main__':
    print("Attempting to delete movies released before 2000...")
    query_year = 2000
    deleted_items = delete_movies_before(query_year)
    print(f"Deleted {len(deleted_items)} movies released before {query_year}.")
