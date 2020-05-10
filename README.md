# Twitter Scraper and Sentiment Analysis
Scrape tweets with Tweepy (requires twitter dev account) and does some basic NLP

Goal: Scrape tweets with hashtag "#COVID19" and perform sentiment analysis on them to make some plots.

## Requirements:
-  Python3.6 or above

## Quickstart:

1)  Create Virtual Environment and Install Libraries (not necessary but recommended)
    ```
    python3 -m venv tweets_venv
    ```
    And access with
    ```
    source activate ./tweets_venv
    ```
    Note: You can exit the virtual environment at any time with `deactivate`.
    Install libraries with
    ```
    python3 -m pip install -r ./requirements.txt
    ```

2) 

## Process Diary:
First Step: Scraping

-  Create a twitter developer account: https://developer.twitter.com/en 
-  Create an app and get api key, api key secret, access key and access_key_secret
-  Enter into `./web_scraper/twitter_keys` template 

Refs:
-  https://realpython.com/twitter-bot-python-tweepy/