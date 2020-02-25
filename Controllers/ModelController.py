# This class will be used as a gateway between the twitter and firestore services, and will perform filtering operations
# on tweet content as well as providing tojson methods for both the sources and news


class ModelController(object):

    def __init__(self):
        self.account_hash_map = {}

    def add_tweet_to_account(self, tweet, username):
        account = self.account_hash_map.get(username)
        account.add_tweets(tweet)
        self.add_or_update_account(account)

    def add_or_update_account(self, account):
        self.account_hash_map.update({account.username: account})

    def get_filtered_tweets_from_account(self, username):
        return self.account_hash_map.get(username).get_tweets()

    def get_accounts(self):
        return self.account_hash_map

    def clear(self):
        self.account_hash_map.clear()
        self.account_hash_map = {}
