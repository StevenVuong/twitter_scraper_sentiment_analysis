import tweepy
import pandas as pd
import logging 
import sys
import csv
import datetime

# TODO: Add src to path
sys.path.append("../")
from logs import logs

logger = logging.getLogger()


def read_twitter_access_keys(csv_filepath: str) -> dict:
    """Reads twitter keys csv and returns a dictionary of twitter keys
    Args:
        - csv_filepath(str)
    Returns:
        - dict with key:value pairs for authentication
    """
    names_keys_matrix = pd.read_csv(csv_filepath, header=None, index_col=None).values

    return dict(names_keys_matrix)


def get_twitter_api_object(twitter_keys_dict: dict) -> tweepy.API:
    """ Authenticate our twitter dev credentials and create an api object.
    Also verifies credentials.
    Args:
        - twitter_keys_dict(dict)
    Returns:
        - api_object

    Ref: http://docs.tweepy.org/en/latest/getting_started.html
    """
    # authenticate
    auth = tweepy.OAuthHandler(
        twitter_keys_dict['api_key'],
        twitter_keys_dict['api_key_secret'],
        )
    auth.set_access_token(
        twitter_keys_dict['access_token'],
        twitter_keys_dict['access_token_secret']
        )

    # create API object
    api = tweepy.API(
        auth, 
        wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True
        )

    try:
        api.verify_credentials()
        logger.info("Authentication OK")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        logger.info("Error during authentication")

    return api


# TODO: Set config for csv savepath and cursor options
def extract_query_to_csv(
    twitter_api:tweepy.API, 
    query:str, 
    csv_savepath:str,
    counts:int = 100,
    max_tweets:int= 200
    ):
    """For a given query string, searches twitter and extracts items related
    Then saves to csvfile.
    Args:
        - twitter_api(tweepy.API): Authenticated witter API Object
        - query(str): Matching query to search, E.g.: https://twitter.com/<QUERY>
        - csv_savepath(str)
        - counts(int): Default number of retries to attempt when err occurs
        - max_tweets(int): How many tweets to retrieve

    Refs: 
        - https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
        - Twitter Object: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    """
    # Open/Create a file to append data
    csv_file = open(csv_savepath, 'a')
    csv_writer = csv.writer(csv_file)
    header = ["a"]
    csv_writer.writerow(header)

    # Only able to extract tweets 7 days ago
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    formatted_week_ago = "{0}-{1:02d}-{2:02d}".format(
        week_ago.year,
        week_ago.month, 
        week_ago.day
        )

    # Extract tweets to csv
    for tweet in tweepy.Cursor(
        twitter_api.search, 
        count=100,
        lang="en",
        since=formatted_week_ago
        ).items(max_tweets):

            print(tweet.created_at, tweet.text)
            tweet.coordinates
            tweet.retweet_count
            tweet.favorite_count
            tweet.user.description
            tweet.user.followers_count
            tweet.user.statuses_count
            tweet.user.created_at
            tweet.user.verified
            #csv_writer.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
    csv_file.close()


def main():

    twitter_keys_dict = read_twitter_access_keys("./twitter_keys/twitter_keys.csv")
    twitter_api = get_twitter_api_object(twitter_keys_dict)

    extract_query_to_csv(twitter_api, "COVID19", "/Users/steven/Downloads/tweets.csv")


if __name__ == '__main__':

    logger.setLevel(logging.INFO)
    logs.add_stream_handler(logger)

    try:
        main()

    except Exception as error:
        logger.exception("Unhandled main exception:")
        raise error
    