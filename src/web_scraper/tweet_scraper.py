import tweepy
import pandas as pd
import logging 
import sys

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


def get_twitter_api_object(twitter_keys_dict: dict):
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


def extract_tweets_to_csv():
    """For a given 
    """

    # Ref: https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c

    # Open/Create a file to append data
    csvFile = open('tweets.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    # TODO: What is this actually doing?
    for tweet in tweepy.Cursor(
        api.search, 
        q=query_hashtag, 
        count=100,
        lang="en",
        since="2019-06-01"
        ).items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


def main():

    twitter_keys_dict = read_twitter_access_keys("./twitter_keys/twitter_keys.csv")
    twitter_api = get_twitter_api_object(twitter_keys_dict)


if __name__ == '__main__':

    logger.setLevel(logging.INFO)
    logs.add_stream_handler(logger)

    try:
        main()

    except Exception as error:
        logger.exception("Unhandled main exception:")
        raise error
    