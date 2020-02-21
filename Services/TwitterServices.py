# This class will handle tweet fetching by using the twitter api
import json
import os
from twitter_scraper import get_tweets
from twitter_scraper import Profile


class TwitterServices:

    def __init__(self, accounts_resource, user_tweet_map_resource):
        self.accounts_resource = accounts_resource  # sets the path for the resource
        self.user_tweet_map_resource = user_tweet_map_resource
        self.user_tweet_map = self.init_map()  # inits the map of (account , last fetched tweet id)

    def get_account_names_from_source(self):
        with open(self.accounts_resource) as json_file:
            data = json.load(json_file)
            account_list = data["accountNames"]
        return account_list

    def init_map(self):
        user_tweet_map = self.load_map_from_resources()
        if user_tweet_map is not None:
            return user_tweet_map
        else:
            account_names = self.get_account_names_from_source()
            user_tweet_map = {}
            for name in account_names:
                user_tweet_map.update({name: 0})
            return user_tweet_map

    def save_map_to_resources(self, user_tweet_map, resource):
        with open(resource, 'w') as outfile:
            json.dump(user_tweet_map, outfile)


    def load_map_from_resources(self):
        if os.stat(self.user_tweet_map_resource).st_size == 0:
            return None
        else:
            with open(self.user_tweet_map_resource) as json_file:
                return json.load(json_file)

    def update_map(self, account_name, last_fetched_tweet_id):  # updates the map after fetch operation on source  done
        return self.user_tweet_map.update({account_name: last_fetched_tweet_id})

    def filter_tweets_since_id(self, tweets, tweet_id):
        def filter_tweets(tweet):
            if int(tweet["tweetId"]) > tweet_id:
                return True
            else:
                return False

        return list(filter(filter_tweets, tweets))

    def fetch_latest_tweets_from_account(self, account_name, number_of_pages, last_fetched_tweet_id):
        tweets = get_tweets(account_name, pages=number_of_pages)
        return self.filter_tweets_since_id(tweets, last_fetched_tweet_id)

    def fetch_account_info(self, account_name):
        return Profile(account_name)
