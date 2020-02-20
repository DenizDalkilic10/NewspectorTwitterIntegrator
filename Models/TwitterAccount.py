# This is the model class of a news source which will store news and other related information about the source
class TwitterAccount(object):

    # instance attributes
    def __init__(self, username, name, followers_count, following_count, likes_count, tweets_count, website,
                 profile_photo, birthday, tweet_list):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.likes_count = likes_count
        self.tweets_count = tweets_count
        self.website = website
        self.profile_photo = profile_photo
        self.birthday = birthday
        self.tweet_list = tweet_list

    def add_tweets(self, tweets):
        self.tweet_list += tweets

    def set_news(self, tweets):
        self.tweet_list = tweets
