# This is the model class of a news
import re


class Tweet(object):

    # instance attributes
    def __init__(self, username, tweet_id, is_retweet, time, text, reply_count, retweet_count, likes, urls,
                 photos, videos):
        self.username = username
        self.tweet_id = tweet_id
        self.is_retweet = is_retweet
        self.time = time
        self.text = text
        self.reply_count = reply_count
        self.retweet_count = retweet_count
        self.likes = likes
        self.urls = urls
        self.photos = photos
        self.videos = videos

    def filter(self, regex):
        self.text = re.sub(regex, "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'^https?:\/\/.*[\r\n]*', '', self.text, flags=re.MULTILINE)
