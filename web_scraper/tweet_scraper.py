import tweepy
import pandas as pd


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
        print("Authentication OK")
    except:
        print("Error during authentication")

    return api


twitter_keys_dict = read_twitter_access_keys("./twitter_keys/twitter_keys.csv")
twitter_api = get_twitter_api_object(twitter_keys_dict)
