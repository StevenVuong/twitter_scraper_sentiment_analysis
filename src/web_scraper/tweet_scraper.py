import tweepy
from pandas import read_csv
import logging 
import sys
import csv
import datetime
import configparser

# TODO: Add src to path
sys.path.append("../")
from logs import logs
from progress.bar import Bar

logger = logging.getLogger()
config = configparser.ConfigParser()
config.read('./config.ini')


def read_twitter_access_keys(csv_filepath: str) -> dict:
    """Reads twitter keys csv and returns a dictionary of twitter keys
    Args:
        - csv_filepath(str)
    Returns:
        - dict with key:value pairs for authentication
    """
    names_keys_matrix = read_csv(csv_filepath, header=None, index_col=None).values

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
        logger.info("Twitter account authentication OK")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        logger.info("Error during authentication")

    return api


def extract_tweets_to_csv(
    twitter_api:tweepy.API, 
    query:str, 
    csv_savepath:str,
    counts:int = 100,
    max_tweets:int= config.getint("web_scraper", "max_tweets")
    ):
    """For a given query string, searches twitter and extracts items related
    to the query sring, then saves to csvfile with the following columns:
        - "tweet_creation_date", 
        - "tweet_text", 
        - "tweet_retweet_count",
        - "tweet_favourite_count",
        - "tweet_hashtags",
        - "user_follow_count",
        - "user_created_at",
        - "user_verified"
    Args:
        - twitter_api(tweepy.API): Authenticated witter API Object
        - query(str): Matching query to search, E.g.: https://twitter.com/<QUERY>
        - csv_savepath(str)
        - counts(int): Default number of retries to attempt when err occurs
        - max_tweets(int): How many tweets to retrieve
    Note:
        - Can only extract tweets 7 days prior
        - Cap on number of calls we can make to the API. About 900 per 15 mins
        and automatically sleeps before resuming if limit is exceeded.
        - A user account is verified if deemed to be of public interest
    Refs: 
        - https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
        - Twitter Object: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
        - Verified Twitter accounts: https://help.twitter.com/en/managing-your-account/about-twitter-verified-accounts
    """
    # open/create a csv to append data
    csv_file = open(csv_savepath, 'a')
    csv_writer = csv.writer(csv_file)
    header = [
        "tweet_creation_date", 
        "tweet_text", 
        "tweet_retweet_count",
        "tweet_favourite_count",
        "tweet_hashtags",
        "user_follow_count",
        "user_created_at",
        "user_verified"
        ]
    csv_writer.writerow(header)

    # Only able to extract tweets up to 7 days ago
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    formatted_week_ago = "{0}-{1:02d}-{2:02d}".format(
        week_ago.year,
        week_ago.month, 
        week_ago.day
        )

    bar = Bar("Loading Tweets", fill="~",max=max_tweets, suffix="%(percent)d%%")
    # extract tweets to csv
    for tweet in tweepy.Cursor(
        twitter_api.search, 
        q=query,
        count=counts,
        lang="en",
        since=formatted_week_ago
        ).items(max_tweets):

        tweet_hashtags = [txt_dict["text"].split(" ")[0] for txt_dict in tweet.entities["hashtags"]]

        row = [
            tweet.created_at,
            tweet.text,
            tweet.retweet_count,
            tweet.favorite_count,
            tweet_hashtags,
            tweet.user.followers_count,
            tweet.user.created_at,
            tweet.user.verified,
            ]
        csv_writer.writerow(row)
        bar.next()
    
    csv_file.close()
    bar.finish()


def main():

    twitter_keys_dict = read_twitter_access_keys("./twitter_keys/twitter_keys.csv")
    twitter_api = get_twitter_api_object(twitter_keys_dict)

    query = config["web_scraper"]["query"]
    tweet_savepath = config["web_scraper"]["csv_savepath"]

    extract_tweets_to_csv(twitter_api, query, tweet_savepath)


if __name__ == '__main__':

    logger.setLevel(logging.INFO)
    logs.add_stream_handler(logger)

    try:
        main()

    except Exception as error:
        logger.exception("Unhandled main exception:")
        raise error
    