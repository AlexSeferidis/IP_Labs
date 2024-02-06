## Print complete information on the movie 'After Hours' Released in 1985 ##

from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

def query_movies(year, title, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')
    response = table.query(
        ProjectionExpression="#yr, #tl, info.genres, info.actors[0]",
        ExpressionAttributeNames={
        "#yr": "year",
        "#tl": "title"
        },
        KeyConditionExpression=Key('year').eq(year) & Key('title').eq(title)
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1985
    query_title = 'After Hours'
    print(f"All info on {query_title}")
    movies = query_movies(query_year, query_title)
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}")
        pprint(movie['info'])