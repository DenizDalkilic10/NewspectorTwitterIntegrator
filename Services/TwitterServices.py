# This class will handle tweet fetching by using the twitter api
import json
from twitter_scraper import get_tweets
from twitter_scraper import Profile


class TwitterServices:

    def __init__(self, account_names_resource):
        self.account_names_resource = account_names_resource  # sets the path for the resource
        self.map = self.init_map()  # inits the map of (account , last fetched tweet id)

    def get_account_names_from_source(self):
        with open(self.account_names_resource) as json_file:
            data = json.load(json_file)
            account_list = data["accountNames"]
        return account_list

    def init_map(self):
        account_names = self.get_account_names_from_source()
        map_of_account_name_and_id = {}
        for name in account_names:
            map_of_account_name_and_id.update({name: 0})
        return map_of_account_name_and_id

    def update_map(self, account_name, last_fetched_tweet_id):  # updates the map after fetch operation on source  done
        return self.map.update({account_name: last_fetched_tweet_id})

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

