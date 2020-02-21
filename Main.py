# This class will call service manager object and perform operations in every xxx minute until shutdown
from Services import TwitterServices

accounts_resource = "Resources/NewsSources.json"
user_tweet_map_resource = "Resources/UserTweetMap.json"

twitter_service = TwitterServices.TwitterServices(accounts_resource, user_tweet_map_resource)

for i in twitter_service.user_tweet_map:
    profile = twitter_service.fetch_account_info(i)
    tweets = twitter_service.fetch_latest_tweets_from_account(i, 1, twitter_service.user_tweet_map[i])
    if len(tweets) != 0:
        twitter_service.update_map(i, int(tweets[0]["tweetId"]))
    for tweet in tweets:
        print("Account: " + i + " | Tweet: " + tweet["text"] + " | " + tweet["tweetId"])
twitter_service.save_map_to_resources(twitter_service.user_tweet_map, user_tweet_map_resource)
