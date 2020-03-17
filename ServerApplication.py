from Models import TwitterAccount
from Models import Tweet
from Services import TwitterServices
from Services import FirestoreServices
from Controllers import ModelController


class ServerApplication(object):

    def __init__(self, accounts_resource, user_tweet_map_resource, firestore_credentials_resource):
        self.accounts_resource = accounts_resource
        self.user_tweet_map_resource = user_tweet_map_resource
        self.firestore_credentials_resource = firestore_credentials_resource
        self.filter_regex = r'breaking\:|update\:|live\:|breaking\||update\||live\||breaking|update|live'
        self.twitter_service = TwitterServices.TwitterServices(self.accounts_resource, self.user_tweet_map_resource)
        self.firestore_service = FirestoreServices.FireStoreServices(self.firestore_credentials_resource);
        self.model_controller = ModelController.ModelController()

    def run(self):
        self.download_accounts()
        self.download_tweets()

        # do any operation needed on models
        self.filter_tweets_from_accounts()
        # do any operation needed on models

        self.upload_accounts()
        self.upload_tweets()

    def download_tweets(self):
        for i in self.twitter_service.user_tweet_map:
            tweets = self.twitter_service.fetch_latest_tweets_from_account(i, 4, self.twitter_service.user_tweet_map[i])

            if len(tweets) != 0:
                for tweet in tweets:
                    t = Tweet.Tweet(i, tweet["tweetId"], tweet["isRetweet"], tweet["time"],
                                    tweet["text"], tweet["replies"], tweet["retweets"], tweet["likes"],
                                    tweet["entries"]["urls"],
                                    tweet["entries"]["photos"],
                                    tweet["entries"]["videos"])
                    self.model_controller.add_tweet_to_account(t, i)
                self.twitter_service.update_map(i, int(tweets[0]["tweetId"]))
            print("Tweets fetched from " + i)
        self.twitter_service.save_map_to_resources(self.twitter_service.user_tweet_map, self.user_tweet_map_resource)

    def upload_tweets(self):
        for account in list(self.model_controller.get_accounts().values()):
            for tweet in account.get_tweets():
                self.firestore_service.add_tweet(tweet)
            print("Tweets uploaded from " + account.username)

    def download_accounts(self):
        for username in self.twitter_service.user_tweet_map:
            profile = self.twitter_service.fetch_account_info(username)
            account = TwitterAccount.TwitterAccount(username, profile.name, profile.followers_count,
                                                    profile.following_count,
                                                    profile.likes_count, profile.tweets_count, profile.website,
                                                    profile.profile_photo,
                                                    profile.birthday, profile.biography, list())
            self.model_controller.add_or_update_account(account)
            print("Account info for " + username + " fetched")

    def upload_accounts(self):
        for account in list(self.model_controller.get_accounts().values()):
            self.firestore_service.add_twitter_account(account)
            print("Account info uploaded for " + account.username + " fetched")

    def filter_tweets_from_accounts(self):
        for account in list(self.model_controller.get_accounts().values()):
            account.filter_tweets(self.filter_regex)
            print("Tweets filtered for " + account.username + " fetched")
