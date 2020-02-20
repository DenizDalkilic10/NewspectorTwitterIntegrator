# This is the model class of a news
class Tweets(object):

    # instance attributes
    def __init__(self, username,tweet_id, is_retweet, link, time, text, reply_count, retweet_count, likes, entries):
        self.username = username
        self.tweet_id = tweet_id
        self.is_retweet = is_retweet
        self.time = time
        self.text = text
        self.reply_count = reply_count
        self.retweet_count = retweet_count
        self.likes = likes
        self.entries = entries


