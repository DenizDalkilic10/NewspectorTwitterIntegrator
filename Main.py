# This class will call service manager object and perform operations in every xxx minute until shutdown
from Services import TwitterServices

twitter_service = TwitterServices.TwitterServices("C:/Users/user/PycharmProjects/NewspectorNewsFetcher/Resources"
                                                  "/NewsSources.json")
for i in twitter_service.map:
    profile = twitter_service.fetch_account_info(i)
    tweets = twitter_service.fetch_latest_tweets_from_account(i, 1, twitter_service.map[i])
    # for tweet in tweets:
    #     print(i + " " + tweet["tweetId"])
    twitter_service.update_map(i, int(tweets[len(tweets)-1]["tweetId"]))
    #print(twitter_service.map)