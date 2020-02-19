# This class will call service manager object and perform operations in every xxx minute until shutdown
from Services import TwitterServices

twitter_service = TwitterServices.TwitterServices("C:/Users/user/PycharmProjects/NewspectorNewsFetcher/Resources"
                                                  "/NewsSources.json")
for i in twitter_service.map:
    for tweet in twitter_service.fetch_latest_tweets_from_account(i, 1, twitter_service.map[i]):
        print(i + " " + tweet["tweetId"])


#
