# This class will handle the integration with firestore and uploading documents to it

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import DocumentReference


class FireStoreServices(object):

    def __init__(self, credentials_resource):
        self.cred = credentials.Certificate(credentials_resource)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def add_twitter_account(self, account):
        account_data = {
            'username': account.username,
            'name': account.name,
            'followers_count': account.followers_count,
            'following_count': account.following_count,
            'likes_count': account.likes_count,
            'tweets_count': account.tweets_count,
            'website': account.website,
            'profile_photo': account.profile_photo,
            'birthday': account.birthday,
        }
        self.db.collection('accounts').document(account.username).set(account_data)

    def add_tweet(self, tweet):
        tweet_data = {
            'username': tweet.username,
            'userRef': self.db.collection("accounts").document(tweet.username),
            'tweet_id': tweet.tweet_id,
            'is_retweet': tweet.is_retweet,
            'time': tweet.time,
            'text': tweet.text,
            'reply_count': tweet.reply_count,
            'retweet_count': tweet.retweet_count,
            'likes': tweet.likes,
            'urls': tweet.urls,
            'photos': tweet.photos,
            'videos': tweet.videos
        }
        self.db.collection('tweets').document(tweet.tweet_id).set(tweet_data)
