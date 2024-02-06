## Print only the years and titles of movies staring Tom Hanks ##

from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr

def scan_movies(actor_name, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')

    # Scan with a filter expression to find movies where Tom Hanks is one of the actors
    response = table.scan(
        FilterExpression=Attr('info.actors').contains(actor_name)
    )
    
    data = response['Items']
    display_movies(data)

    # Continue scanning if there are more pages of results
    while 'LastEvaluatedKey' in response:
        response = table.scan(
            FilterExpression=Attr('info.actors').contains(actor_name),
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        data.extend(response['Items'])
        display_movies(data)

    return data

if __name__ == '__main__':
    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}")

    query_actor = 'Tom Hanks'
    print(f"Scanning for movies starring {query_actor} ...")
    scan_movies(query_actor, print_movies)
