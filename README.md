# Twitter Scraper and Sentiment Analysis
Scrape tweets with Tweepy (requires twitter dev account) and does some basic NLP

Goal: Scrape tweets with hashtag "#COVID19" and perform sentiment analysis on them to make some plots.
See how many correlate to food shortage.

###  Requirements:
-  Python3.6 or above

## Overview & Getting Started:

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

2)  Extract tweets: 
    ```
    cd ./src/web_scraper/
    ```
    1) Authentication:
    - Create a twitter developer account: https://developer.twitter.com/en 
    -  Create an app and get api key, api key secret, access key and access_key_secret
    -  Enter into `./twitter_keys_template.csv` and then rename the file to 
    `twitter_keys.csv`. <br>
    **Recommended:** to rename as twitter_keys.csv is in the `.gitignore`.
    2) Update `./config` with desired query, save path and maximum number of tweets to extract.<br>
    Query goes: https://twitter.com/<QUERY>
    3) Run: 
    ```
    tweet_scraper.py
    ```

    4) We then find the following columns in our saved csvfile:
        -  "tweet_creation_date", 
        -  "tweet_text", 
        -  "tweet_retweet_count",
        -  "tweet_favourite_count",
        -  "tweet_hashtags",
        -  "user_follow_count",
        -  "user_created_at",
        -  "user_verified"

    Note:
    -  Can only extract tweets up to 7 days prior
    -  Cap on number of calls we can make to the API. About 900 per 15 mins
        and automatically sleeps before resuming if limit is exceeded.
    -  A user account is verified if deemed to be of public interest

3) Sentiment Analysis:
    To launch a jupyter notebook:
    ```
    cd ./src/tweet_eda/
    jupyter notebook .
    ```
    Which should prompt your default browser application to open a jupyter notebook
    instance (http://localhost:8888/notebooks)

    Note:
    - For maintainability purposes, we will be saving jupyter notebooks with no outputs

Compare density of tweetts.
Maybe extract what relates to food, compare frequency. Use hashtags
sentiment.
country names etc..
Kaggle for cleaning and analysis kernels
Hashtag for analysis
Extract and clean tweets first. Look at dataset


### Process Diary: 
For times of procrastination. -> To be filled
